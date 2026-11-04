#!/usr/bin/env python3
"""公開前チェック。python3 check.py [--visual]
エラー(ERROR)が1つでもあれば終了コード1。警告(WARN)は目視で確認する。"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).parent
errors, warns = [], []
def err(m): errors.append(m)
def warn(m): warns.append(m)

b = subprocess.run([sys.executable, "build.py"], cwd=ROOT, capture_output=True, text=True)
if b.returncode != 0:
    err("build.py 失敗: " + (b.stderr or b.stdout)[-300:])
site = json.loads((ROOT / "config/site.json").read_text(encoding="utf-8"))
docs = sorted((ROOT / "docs").rglob("*.html"))
tips = sorted((ROOT / "content/tips").glob("*.md"))
news = sorted((ROOT / "content/news").glob("*.md"))
queue = json.loads((ROOT / "data/queue.json").read_text(encoding="utf-8"))
def text_of(p): return p.read_text(encoding="utf-8")

# 1. 個人情報・非公開情報
targets = docs + tips + news + [ROOT / "README.md", ROOT / "config/site.json", ROOT / "data/queue.json"]
for p in targets:
    t = text_of(p)
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]+", t):
        if "users.noreply.github.com" in m.group(0):
            continue
        err(f"メールアドレスらしき文字列 {m.group(0)!r}: {p.relative_to(ROOT)}")
private_words = ["運営メモ", "自分への応用", "hiragana-town", "注目銘柄", "稼ぎのトリセツ", "kasegi"]
for p in docs + tips + news:
    t = text_of(p)
    for w in private_words:
        if w in t:
            err(f"非公開・別サイトに関わる語 {w!r}: {p.relative_to(ROOT)}")


# 用語解説: 形式と、各ページのリンク先の確認
glossary = json.loads((ROOT / "data/glossary.json").read_text(encoding="utf-8"))
gids = [g["id"] for g in glossary]
if len(gids) != len(set(gids)):
    err("data/glossary.json: id が重複している")
for g in glossary:
    for k in ("id", "term", "category", "explain"):
        if not g.get(k):
            err(f"data/glossary.json: {g.get('id')} に {k} がない")
for p in docs:
    for m in re.finditer(r'href="(?:\.\./)?glossary/#term-([a-z0-9-]+)"', text_of(p)):
        if m.group(1) not in gids:
            err(f"用語解説にない用語へのリンク {m.group(1)}: {p.relative_to(ROOT)}")

# 2. 表現
hard_ban = [r"1日1[つ手]", r"毎日更新", r"毎日1[つ手]", r"毎朝8時に更新", r"1日1ページ"]
soft_ban = [r"必ず(うまく|成功|稼)", r"絶対に?(うまく|成功|稼)", r"誰でも簡単に", r"完璧に", r"100%正確", r"ノーリスク"]
for p in docs:
    t = re.sub(r"<[^>]+>", "", text_of(p))
    for pat in hard_ban:
        if re.search(pat, t):
            err(f"更新頻度の説明 {pat}: {p.relative_to(ROOT)}")
    for pat in soft_ban:
        for m in re.finditer(pat, t):
            s = t[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
            warn(f"断定的な表現(確認) {pat}: {p.relative_to(ROOT)} …{s}…")

# 3. 広告・アフィリエイト・非公式表記
ads = site.get("ads", {})
if not ads.get("enabled") and not ads.get("placeholder"):
    for p in docs:
        if "ad-slot" in text_of(p) or "広告スペース" in text_of(p):
            err(f"広告枠の表示が残っている: {p.relative_to(ROOT)}")
if ads.get("enabled") or site.get("affiliate", {}).get("amazon_tag"):
    if not any("広告について" in text_of(p) for p in docs):
        err("広告/アフィリエイトが有効なのに「広告について」の表記がない")
for p in docs:
    if "非公式のサイト" not in text_of(p):
        err(f"非公式である旨の表記がない: {p.relative_to(ROOT)}")

# 4. 原稿ごとの必須項目
for p in tips + news:
    t = text_of(p)
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    if not m:
        err(f"フロントマターなし: {p.name}"); continue
    fm, body = m.group(1), m.group(2)
    urls = re.findall(r"https?://[^\s|]+", fm)
    if len(urls) < 1:
        err(f"出典URLなし: {p.name}")
    is_tip = p.parent.name == "tips"
    heads = re.findall(r"^## (.+)$", body, re.M)
    if is_tip:
        for need in ("ねらい", "準備", "手順", "うまくいかない"):
            if not any(need in h for h in heads):
                err(f"必須の見出し「{need}」なし: {p.name}")
        if ":::prompt" not in body:
            err(f"そのまま使えるプロンプト(:::prompt)なし: {p.name}")
        if ":::flow" not in body:
            warn(f"手順の図(:::flow)なし: {p.name}")
        if not re.search(r"^next:", fm, re.M):
            warn(f"次のステップ(next)なし: {p.name}")
    else:
        for need in ("何が", "活用方法", "注意"):
            if not any(need in h for h in heads):
                err(f"最新情報の必須の見出し「{need}」なし: {p.name}")
    for line in re.findall(r"^- (.+\| [^|]*\| ?[0-9Xx-]+)$", fm, re.M):
        isbn = re.sub(r"[^0-9Xx]", "", line.split("|")[-1])
        if len(isbn) == 13:
            s = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(isbn[:12]))
            if (10 - s % 10) % 10 != int(isbn[12]):
                err(f"ISBNのチェックデジットが合わない {isbn}: {p.name}")
        else:
            err(f"ISBNが13桁でない {isbn}: {p.name}")
    nbooks = len(re.findall(r"^books:", fm, re.M)) and len(re.findall(r"\| *97[89][0-9-]{10,}$", fm, re.M))
    if nbooks and nbooks > 4:
        warn(f"紹介本が多い({nbooks}冊): {p.name}")

# 5. queue
slugs = [q["slug"] for q in queue]
if len(slugs) != len(set(slugs)):
    err("queue.json に slug の重複がある")
for q in queue:
    if q["level"] not in {l["id"] for l in site["levels"]}: err(f"queue: 不明な難易度 {q['slug']}")
    if q["purpose"] not in {l["id"] for l in site["purposes"]}: err(f"queue: 不明な目的 {q['slug']}")
    for f in q["features"]:
        if f not in {l["id"] for l in site["features"]}: err(f"queue: 不明な機能 {q['slug']} {f}")
for p in tips:
    if p.stem not in slugs:
        warn(f"queue.json にない活用方法: {p.stem}")

# 6. 内部リンク切れ
for p in docs:
    for href in re.findall(r'href="([^"#:]+?)"', text_of(p)):
        if href.startswith(("http", "mailto")) or re.search(r"[\'\"+ ]", href): continue
        tgt = (p.parent / href).resolve()
        if tgt.is_dir(): tgt = tgt / "index.html"
        if not tgt.exists():
            err(f"リンク切れ {href}: {p.relative_to(ROOT)}")

# 7. 見た目(任意)
if "--visual" in sys.argv:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 390, "height": 800})
        for p in docs:
            pg.goto(p.resolve().as_uri())
            w = pg.evaluate("document.documentElement.scrollWidth")
            if w > 392: err(f"横スクロール発生({w}px): {p.relative_to(ROOT)}")
        br.close()

for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"\n{len(errors)} errors, {len(warns)} warnings, {len(docs)} html pages")
sys.exit(1 if errors else 0)
