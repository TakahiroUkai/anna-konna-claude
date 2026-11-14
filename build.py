#!/usr/bin/env python3
"""あんなことこんなことClaude 静的サイト生成(標準ライブラリのみ)。

使い方:
  python3 build.py                 content/ から docs/ を再生成する
  python3 build.py --next          次に追加する活用方法(data/queue.json の先頭の未掲載)を表示する
  python3 build.py --archive-json  公開済みの全ページの情報をJSONで出力する(非公開アーカイブ用)
"""
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
TIPS_DIR = ROOT / "content" / "tips"
NEWS_DIR = ROOT / "content" / "news"
GUIDES_DIR = ROOT / "content" / "guides"
DOCS = ROOT / "docs"
NOGA = (
    '<script>(function(){try{var m=location.search.match(/[?&]noga=([01])/),k="noga",id="G-MS9416YMMM";'
    'if(m){if(m[1]=="1")localStorage.setItem(k,"1");else localStorage.removeItem(k);'
    'var f=function(){var d=document.createElement("div");d.setAttribute("role","status");'
    'd.style.cssText="position:fixed;left:8px;right:8px;bottom:8px;z-index:99;padding:10px 14px;background:#222;color:#fff;border-radius:8px;font:14px sans-serif;text-align:center";'
    'd.textContent=m[1]=="1"?"この端末のブラウザを、アクセス解析から除外しました":"この端末のブラウザの、アクセス解析の除外をやめました";'
    'document.body.appendChild(d);setTimeout(function(){d.remove()},4000)};'
    'if(document.body)f();else addEventListener("DOMContentLoaded",f)}'
    'if(localStorage.getItem(k)=="1")window["ga-disable-"+id]=true}catch(e){}})();</script>'
)
GA_TAG = (
    NOGA +
    '<script async src="https://www.googletagmanager.com/gtag/js?id=G-MS9416YMMM"></script>'
    '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    "gtag('js',new Date());gtag('config','G-MS9416YMMM');</script>"
)
CONFIG = json.loads((ROOT / "config" / "site.json").read_text(encoding="utf-8"))
QUEUE = json.loads((ROOT / "data" / "queue.json").read_text(encoding="utf-8"))
GLOSSARY = json.loads((ROOT / "data" / "glossary.json").read_text(encoding="utf-8"))
_TERM_ID = {w: g["id"] for g in GLOSSARY for w in g.get("link", [])}
_TERM_RE = re.compile("|".join(re.escape(w) for w in sorted(_TERM_ID, key=len, reverse=True))) if _TERM_ID else None
_LINKER = {"root": None, "seen": set()}

LEVELS = {l["id"]: l for l in CONFIG["levels"]}
PURPOSES = {p["id"]: p for p in CONFIG["purposes"]}
FEATURES = {f["id"]: f for f in CONFIG["features"]}
GUIDE_TOPICS = {t["id"]: t for t in CONFIG.get("guide_topics", [])}

LIST_KEYS = ("books", "sources")
TIP_REQUIRED = ["title", "level", "minutes", "purpose", "features", "output", "summary", "added", "updated"]
NEWS_REQUIRED = ["title", "date", "summary", "added", "updated"]
GUIDE_REQUIRED = ["title", "summary", "topic", "minutes", "added", "updated"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def esc(s):
    return html.escape(str(s), quote=True)


# ---------- 読み込み ----------

def parse_front(text, name, required, kind):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"{name}: 先頭の --- で囲んだメタ情報がありません")
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("- ") and key in LIST_KEYS:
            meta[key].append([p.strip() for p in line[2:].split(" | ")])
        else:
            k, _, v = line.partition(":")
            key, v = k.strip(), v.strip()
            meta[key] = [] if (key in LIST_KEYS and not v) else v
    for k in required:
        if not meta.get(k):
            raise SystemExit(f"{name}: メタ情報 {k} がありません")
    if not meta.get("sources"):
        raise SystemExit(f"{name}: sources(出典)が1件もありません。調べた情報源を載せてください")
    for k in ("added", "updated", "date"):
        if meta.get(k) and not DATE_RE.match(meta[k]):
            raise SystemExit(f"{name}: {k} は YYYY-MM-DD の形式にしてください")
    meta["features"] = [x.strip() for x in meta.get("features", "").split(",") if x.strip()]
    meta["next"] = [x.strip() for x in meta.get("next", "").split(",") if x.strip()]
    for f in meta["features"]:
        if f not in FEATURES:
            raise SystemExit(f"{name}: 不明な機能タグ {f}(config/site.json の features にありません)")
    if kind == "guide":
        if meta["topic"] not in GUIDE_TOPICS:
            raise SystemExit(f"{name}: 不明な解説の分類 {meta['topic']}(config/site.json の guide_topics にありません)")
        try:
            meta["minutes"] = int(meta["minutes"])
        except ValueError:
            raise SystemExit(f"{name}: minutes は整数にしてください")
    if kind == "tip":
        if meta["level"] not in LEVELS:
            raise SystemExit(f"{name}: 不明な難易度 {meta['level']}")
        if meta["purpose"] not in PURPOSES:
            raise SystemExit(f"{name}: 不明な目的 {meta['purpose']}")
        try:
            meta["minutes"] = int(meta["minutes"])
        except ValueError:
            raise SystemExit(f"{name}: minutes は整数にしてください")
    return meta, m.group(2)


def load_dir(directory, required, kind):
    items = {}
    for p in sorted(directory.glob("*.md")):
        meta, body = parse_front(p.read_text(encoding="utf-8"), p.name, required, kind)
        meta["slug"] = p.stem
        meta["body"] = body
        meta["kind"] = kind
        items[p.stem] = meta
    return items


# ---------- 簡易Markdown ----------

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)

    def link(m):
        url = m.group(2).replace('"', "%22")
        if not re.match(r"^(https?://|\.{0,2}/|#)", url):
            return m.group(0)
        ext = ' rel="noopener" target="_blank"' if url.startswith("http") else ""
        return f'<a href="{url}"{ext}>{m.group(1)}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)


def lt(h):
    """inline()後のHTML本文のうち、用語解説にある語の、ページ内の最初の1回だけをリンクにする。"""
    root = _LINKER["root"]
    if root is None or _TERM_RE is None:
        return h
    out, depth = [], 0
    for part in re.split(r"(<[^>]+>)", h):
        if part.startswith("<"):
            if re.match(r"<(a|code)\b", part):
                depth += 1
            elif re.match(r"</(a|code)>", part):
                depth -= 1
            out.append(part)
            continue
        if depth > 0:
            out.append(part)
            continue

        def rep(m):
            gid = _TERM_ID[m.group(0)]
            if gid in _LINKER["seen"]:
                return m.group(0)
            _LINKER["seen"].add(gid)
            return f'<a class="term" href="{root}glossary/#term-{gid}">{m.group(0)}</a>'

        out.append(_TERM_RE.sub(rep, part))
    return "".join(out)


def to_blocks(md):
    blocks, para, items, kind = [], [], [], None

    def flush():
        nonlocal para, items, kind
        if para:
            blocks.append(("p", " ".join(para)))
        if items:
            blocks.append((kind, items))
        para, items, kind = [], [], None

    fence = None
    for raw in md.strip("\n").splitlines():
        s = raw.strip()
        if fence is not None:
            if s == ":::":
                blocks.append(("fig", (fence[0], fence[1])))
                fence = None
            else:
                fence[1].append(raw.rstrip())
            continue
        if s.startswith(":::"):
            flush()
            fence = (s[3:].strip(), [])
        elif not s:
            flush()
        elif s.startswith("## "):
            flush(); blocks.append(("h2", s[3:]))
        elif s.startswith("### "):
            flush(); blocks.append(("h3", s[4:]))
        elif re.match(r"^[-*] ", s):
            if kind != "ul":
                flush()
            kind = "ul"; items.append(s[2:])
        elif re.match(r"^\d+\. ", s):
            if kind != "ol":
                flush()
            kind = "ol"; items.append(re.sub(r"^\d+\. ", "", s))
        else:
            if items:
                flush()
            para.append(s)
    flush()
    return blocks


PH_LINE = re.compile(r"^\s*[（(](?!\d+[）)]).*[）)]\s*$")
PH_INLINE = re.compile(
    r"(?<!「)[（(](?:例[::]|ここに)[^（）()\n]*[）)]"      # (例: …)(ここに…)
    r"|[（(][^（）()\n]*(?:を|ここに)貼る[）)]"           # (…を貼る)
    r"|(?<=[::])\s*[（(][^（）()\n]*[）)]\s*$"          # 「項目: (…)」で行が終わる
    r"|[（(]例[）)][^\n]*$"                              # (例)… 行末まで
    r"|[（(](?:話題の名前|テーマ)[）)]")                   # 「(話題の名前)」のような、かぎ括弧の中の差し替え


def mark_placeholders(text):
    """プロンプトの中の、書き換える部分(括弧つき)に目印を付ける。戻り値は (HTML, 箇所の数)。"""
    out, n = [], 0
    for line in text.split("\n"):
        if PH_LINE.match(line):
            lead = line[:len(line) - len(line.lstrip())]
            out.append(esc(lead) + '<mark class="ph">' + esc(line.strip()) + "</mark>")
            n += 1
            continue
        pos, buf = 0, ""
        for m in PH_INLINE.finditer(line):
            g = m.group(0)
            pad = g[:len(g) - len(g.lstrip())]
            buf += esc(line[pos:m.start()]) + esc(pad) + '<mark class="ph">' + esc(g.strip()) + "</mark>"
            tail = g[len(g.rstrip()):]
            buf += esc(tail)
            pos = m.end()
            n += 1
        out.append(buf + esc(line[pos:]))
    return "\n".join(out), n


def render_fig(head, lines):
    """図・部品ブロック。
    :::flow 見出し      行: 見出し | 補足            (手順の流れ)
    :::prompt 見出し    行: そのまま使う文章(空行も保持。コピーボタンつき)
    :::compare 見出し   行: 左 | 右 (1行目は表の見出し)
    :::note 見出し      行: 注意書きの段落
    """
    kind, _, title = head.partition(" ")
    cap = f"<figcaption>{inline(title)}</figcaption>" if title else ""
    if kind == "prompt":
        text = "\n".join(lines).strip("\n")
        code, n = mark_placeholders(text)
        bar = f"色のついた{n}か所を書き換えてから使います" if n else "そのまま貼って使えます"
        return (f'<figure class="fig fig-prompt">{cap}<div class="prompt">'
                f'<div class="prompt-bar"><span>{bar}</span>'
                f'<button type="button" class="copy" data-copy>コピー</button></div>'
                f'<pre><code>{code}</code></pre></div></figure>')
    if kind == "svg":
        return f'<figure class="fig fig-svg">{cap}{chr(10).join(lines).strip()}</figure>'
    if kind == "output":
        text = "\n".join(lines).strip("\n")
        return (f'<figure class="fig fig-output">{cap}<div class="output">'
                f'<div class="output-bar"><span>実際に出力された例(実行のたびに結果は変わります)</span></div>'
                f'<pre><code>{esc(text)}</code></pre></div></figure>')
    rows = [[c.strip() for c in l.split("|")] for l in lines if l.strip()]
    if kind == "table":
        head_row, body_rows = rows[0], rows[1:]
        col = {"Cowork": "cw", "Claude Code": "cc", "チャット": "ch"}
        cls = [f' class="c-{col[h]}"' if h in col else "" for h in head_row]
        th = "".join(f'<th scope="col"{cls[i]}>{inline(c)}</th>' for i, c in enumerate(head_row))
        tb = ""
        for r in body_rows:
            cells = ""
            for i, c in enumerate(r):
                if i == 0:
                    cells += f'<th scope="row">{lt(inline(c))}</th>'
                else:
                    label = head_row[i] if i < len(head_row) else ""
                    c_cls = cls[i] if i < len(cls) else ""
                    cells += f'<td{c_cls} data-label="{esc(label)}">{lt(inline(c))}</td>'
            tb += f"<tr>{cells}</tr>"
        return f'<figure class="fig fig-table">{cap}<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></figure>'
    if kind == "flow":
        li = "".join(
            f"<li><strong>{lt(inline(r[0]))}</strong>" + (f"<span>{lt(inline(r[1]))}</span>" if len(r) > 1 and r[1] else "") + "</li>"
            for r in rows
        )
        return f'<figure class="fig fig-flow">{cap}<ol class="flow">{li}</ol></figure>'
    if kind == "compare":
        head_row, body_rows = rows[0], rows[1:]
        th = "".join(f'<th scope="col">{inline(c)}</th>' for c in head_row)
        tb = "".join("<tr>" + "".join(f"<td>{lt(inline(c))}</td>" for c in r) + "</tr>" for r in body_rows)
        return f'<figure class="fig fig-compare">{cap}<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></figure>'
    if kind == "note":
        ps = "".join(f"<p>{inline(' | '.join(r))}</p>" for r in rows)
        return f'<aside class="note">{cap}{ps}</aside>'
    raise SystemExit(f"不明な図の種類: {kind}")


def block_html(b):
    t, c = b
    if t == "fig":
        return render_fig(*c)
    if t == "h3":
        return f"<h3>{inline(c)}</h3>"
    if t == "p":
        return f"<p>{lt(inline(c))}</p>"
    tag = "ul" if t == "ul" else "ol"
    return f"<{tag}>" + "".join(f"<li>{lt(inline(i))}</li>" for i in c) + f"</{tag}>"


def section_class(title):
    if title.startswith(("注意", "共有する前の注意")) or "注意" in title:
        return "warn"
    if "手順" in title:
        return "steps"
    if "うまくいかない" in title:
        return "trouble"
    return ""


def render_body(md, root=None):
    _LINKER["root"] = root
    _LINKER["seen"] = set()
    sections, cur = [], {"title": None, "blocks": []}
    for b in to_blocks(md):
        if b[0] == "h2":
            sections.append(cur)
            cur = {"title": b[1], "blocks": []}
        else:
            cur["blocks"].append(b)
    sections.append(cur)

    out, nav, n = [], [], 0
    for sec in sections:
        inner = "".join(block_html(b) for b in sec["blocks"])
        if sec["title"] is None:
            out.append(inner)
            continue
        n += 1
        sid = f"s{n}"
        nav.append((sid, sec["title"]))
        cls = section_class(sec["title"])
        out.append(f'<section id="{sid}"{f" class=\"{cls}\"" if cls else ""}><h2>{inline(sec["title"])}</h2>{inner}</section>')
        if n == 3 and len(sections) >= 6:
            out.append(ad_slot())
    return "".join(out), nav


# ---------- 部品 ----------

def ad_slot():
    ads = CONFIG.get("ads", {})
    if not ads.get("enabled"):
        if ads.get("placeholder"):
            return '<aside class="ad-slot is-empty" aria-label="広告"><span>広告スペース(準備中)</span></aside>'
        return ""
    snippet = ""
    f = ROOT / ads.get("snippet_file", "")
    if f.is_file():
        snippet = f.read_text(encoding="utf-8")
    return f'<aside class="ad-slot" aria-label="広告">{snippet}</aside>'


def affiliate_on():
    return bool(CONFIG.get("affiliate", {}).get("amazon_tag"))


def book_item(b):
    title = b[0]
    author = b[1] if len(b) > 1 else ""
    isbn = re.sub(r"[^0-9Xx]", "", b[2]) if len(b) > 2 else ""
    tag = CONFIG.get("affiliate", {}).get("amazon_tag", "")
    name = esc(title)
    if tag and isbn:
        url = f"https://www.amazon.co.jp/s?k={esc(isbn)}&amp;tag={esc(tag)}"
        name = f'<a href="{url}" rel="sponsored noopener" target="_blank">{name}</a>'
    by = f'<div class="by">{esc(author)}</div>' if author else ""
    return f"<li>{name}{by}</li>"


def level_chip(level):
    return f'<span class="chip lv-{esc(level)}">{esc(LEVELS[level]["name"])}</span>'


def tag_url(kind, tid, root):
    return f"{root}tags/{kind}-{tid}.html"


def card(t, root):
    """活用方法のカード(一覧用)。"""
    feats = " ".join(t["features"])
    text = " ".join([t["title"], t["summary"], PURPOSES[t["purpose"]]["name"]] + [FEATURES[f]["name"] for f in t["features"]])
    chips = (
        level_chip(t["level"])
        + f'<span class="chip">約{t["minutes"]}分</span>'
        + f'<span class="chip">{esc(PURPOSES[t["purpose"]]["name"])}</span>'
        + "".join(f'<span class="chip chip-f">{esc(FEATURES[f]["name"])}</span>' for f in t["features"])
    )
    return (
        f'<li class="card" data-level="{esc(t["level"])}" data-purpose="{esc(t["purpose"])}" data-features="{esc(feats)}" data-text="{esc(text.lower())}">'
        f'<a class="card-title" href="{root}tips/{esc(t["slug"])}.html">{esc(t["title"])}</a>'
        f'<p class="card-sum">{esc(t["summary"])}</p><p class="chips">{chips}</p></li>'
    )


def news_card(n, root):
    chips = "".join(f'<span class="chip chip-f">{esc(FEATURES[f]["name"])}</span>' for f in n["features"])
    return (
        f'<li class="card card-news"><p class="card-date">{esc(n["date"])} の発表</p>'
        f'<a class="card-title" href="{root}news/{esc(n["slug"])}.html">{esc(n["title"])}</a>'
        f'<p class="card-sum">{esc(n["summary"])}</p><p class="chips">{chips}</p></li>'
    )


def share_block(title, path):
    """SNS共有ボタン。外部の共有スクリプトは読み込まず、各サービスの共有URLへのリンクにする。"""
    url = CONFIG["base_url"] + path
    text = title if title == CONFIG["name"] else f"{title} | {CONFIG['name']}"
    u, t = quote(url, safe=""), quote(text, safe="")
    links = [
        ("share-x", "X", f"https://x.com/intent/post?url={u}&amp;text={t}"),
        ("share-line", "LINE", f"https://social-plugins.line.me/lineit/share?url={u}"),
        ("share-fb", "Facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}"),
        ("share-hb", "はてなブックマーク", f"https://b.hatena.ne.jp/add?mode=confirm&amp;url={u}&amp;title={t}"),
    ]
    items = "".join(
        f'<li><a class="share-btn {c}" href="{h}" target="_blank" rel="noopener noreferrer">{n}<span class="sr-only">で共有(新しいタブで開きます)</span></a></li>'
        for c, n, h in links
    )
    return (
        f'<aside class="share" aria-labelledby="share-h" data-url="{esc(url)}" data-title="{esc(text)}">'
        f'<h2 id="share-h">このページを共有する</h2><ul class="share-list">{items}'
        '<li><button type="button" class="share-btn share-copy">リンクをコピー</button></li>'
        '<li class="share-native" hidden><button type="button" class="share-btn">その他のアプリで共有</button></li>'
        '</ul><p class="share-status" role="status" aria-live="polite"></p></aside>'
    )


def layout(title, desc, body, root, path, article=None, full_title=None):
    name = CONFIG["name"]
    full = full_title or (name if title == name else f"{title} | {name}")
    canon = CONFIG["base_url"] + path
    parts = []
    if affiliate_on():
        parts.append("このサイトには、書籍紹介のアフィリエイトリンク(広告)が含まれます。リンク先で購入されると、運営者に報酬が入ることがあります。")
        parts.append(f"Amazonのアソシエイトとして、{name}は適格販売により収入を得ています。")
    if CONFIG.get("ads", {}).get("enabled"):
        parts.append("広告枠を設けています。")
    og_type = "article" if article else "website"
    meta_extra = ""
    if article:
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
              "datePublished": article["published"], "dateModified": article["modified"], "inLanguage": "ja",
              "mainEntityOfPage": canon, "author": {"@type": "Person", "name": "運営者"},
              "publisher": {"@type": "Organization", "name": name}}
        meta_extra = ('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"
                      f'<meta property="article:published_time" content="{esc(article["published"])}">\n'
                      f'<meta property="article:modified_time" content="{esc(article["modified"])}">\n')
    disclosure = f'<p><strong>広告について</strong> {"".join(parts)}</p>' if parts else ""
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
{GA_TAG}
<script>document.documentElement.className+=' js';</script>
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canon)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{esc(canon)}">
<meta property="og:site_name" content="{esc(name)}">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary">
{meta_extra}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&amp;family=Noto+Serif+JP:wght@500;700&amp;display=swap">
<link rel="stylesheet" href="{root}assets/style.css">
<script src="{root}assets/app.js" defer></script>
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="site-name" href="{root or './'}">{esc(name)}</a>
    <p class="site-tag">{esc(CONFIG["subtitle"])}</p>
    <nav class="site-nav" aria-label="メニュー"><a href="{root or './'}">ホーム</a><a href="{root}guides/">解説</a><a href="{root}news/">Claude最新情報</a><a href="{root}tags/">タグでさがす</a><a href="{root}glossary/">用語解説</a></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <p><strong>このサイトについて</strong> 個人が運営する非公式のサイトです。Anthropic社とは関係ありません。「Claude」はAnthropic社の商標です。</p>
    <p><strong>ご利用にあたって</strong> 一般的な情報の整理であり、結果を保証するものではありません。機能、画面、料金、提供プランは変わることがあるため、各ページの出典(公式情報)と、お使いの画面で確認してください。AIの答えには誤りが含まれることがあります。大事な内容は、自分で確かめてから使ってください。</p>
    {disclosure}
  </div>
</footer>
</body>
</html>
"""


# ---------- ページ生成 ----------

def spec_table(t, root):
    feats = "、".join(f'<a href="{tag_url("feature", f, root)}">{esc(FEATURES[f]["name"])}</a>' for f in t["features"])
    rows = [
        ("難易度", f'<a href="{tag_url("level", t["level"], root)}">{level_chip(t["level"])}</a> {esc(LEVELS[t["level"]]["desc"])}'),
        ("所要時間", f'約{t["minutes"]}分'),
        ("目的", f'<a href="{tag_url("purpose", t["purpose"], root)}">{esc(PURPOSES[t["purpose"]]["name"])}</a>'),
        ("使う機能", feats),
        ("作れるもの", esc(t["output"])),
    ]
    body = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f'<table class="spec"><caption>仕様</caption><tbody>{body}</tbody></table>'


def books_html(m):
    if not m.get("books"):
        return ""
    return ('<section class="books"><h2>この内容を扱っている本</h2><ul class="book-list">'
            + "".join(book_item(b) for b in m["books"]) + "</ul></section>")


def _book_for_source(src, books):
    """書誌情報の出典から、対応する紹介本(書名, ISBN13)を探す。"""
    if "書誌情報" not in src[0]:
        return None
    url = src[1] if len(src) > 1 else ""
    mm = re.search(r"(97[89]\d{10})", url)
    for b in books:
        isbn = re.sub(r"[^0-9Xx]", "", b[2]) if len(b) > 2 else ""
        if not isbn:
            continue
        if mm and isbn == mm.group(1):
            return b[0], isbn
    for b in books:  # URLにISBNが無いときは、書名で対応づける
        isbn = re.sub(r"[^0-9Xx]", "", b[2]) if len(b) > 2 else ""
        if isbn and b[0][:10] in src[0]:
            return b[0], isbn
    return None


def source_item(src, books):
    tag = CONFIG.get("affiliate", {}).get("amazon_tag", "")
    book = _book_for_source(src, books or []) if tag else None
    if book and len(src) > 1:
        title, isbn = book
        store = re.split(r"[「(]", src[0])[0]
        aff = f"https://www.amazon.co.jp/s?k={esc(isbn)}&amp;tag={esc(tag)}"
        return (f'<li><a href="{aff}" rel="sponsored noopener" target="_blank">{esc(title)}(Amazonで見る)</a>'
                f'<span class="by">書誌情報の確認: <a href="{esc(src[1])}" rel="noopener" target="_blank">{esc(store)}</a></span></li>')
    if len(src) > 1:
        return f'<li><a href="{esc(src[1])}" rel="noopener" target="_blank">{esc(src[0])}</a></li>'
    return f"<li>{esc(src[0])}</li>"


def sources_html(m):
    return ('<section class="sources"><h2>調べた情報源</h2><ul class="source-list">'
            + "".join(source_item(s, m.get("books")) for s in m["sources"]) + "</ul></section>")


def related_html(m, tips, root):
    items = [tips[s] for s in m.get("next", []) if s in tips]
    if not items:
        return ""
    return '<section class="related"><h2>つぎに試すなら</h2><ul class="card-list">' + "".join(card(t, root) for t in items) + "</ul></section>"


SISTER_URL = "https://takahiroukai.github.io/kasegi-torisetsu/"


def sister_html():
    """関連の深い別サイト(稼ぎのトリセツ)への案内。許可された組み合わせはこの1か所だけ。"""
    return ('<aside class="sister" aria-labelledby="sister-h"><h2 id="sister-h">あわせて読みたい</h2>'
            f'<p>Claudeで作業を速くしたあとは、副業・個人事業で稼ぐ方法を整理した<a href="{SISTER_URL}" rel="noopener">稼ぎのトリセツ</a>も、読み物として役に立つかもしれません。</p></aside>')


def render_tip(t, tips):
    root = "../"
    body_html, nav = render_body(t["body"], root)
    inpage = "".join(f'<li><a href="#{sid}">{esc(x)}</a></li>' for sid, x in nav)
    page = f"""<div class="wrap doc">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a></p>
    <h1>{esc(t["title"])}</h1>
    <p class="summary">{esc(t["summary"])}</p>
    <p class="stamp">{esc(t["updated"])} 時点の情報</p>
    {spec_table(t, root)}
    <ul class="inpage" aria-label="このページの内容">{inpage}</ul>
  </div>
  {body_html}
  {ad_slot()}
  {related_html(t, tips, root)}
  {sister_html()}
  {books_html(t)}
  {sources_html(t)}
  {share_block(t["title"], f"tips/{t['slug']}.html")}
  <p style="margin-top:2.5rem"><a href="../">ホームにもどる</a></p>
</div>"""
    return layout(t["title"], t["summary"], page, root, f"tips/{t['slug']}.html", {"published": t["added"], "modified": t["updated"]})


def render_news(n, tips):
    root = "../"
    body_html, nav = render_body(n["body"])
    inpage = "".join(f'<li><a href="#{sid}">{esc(x)}</a></li>' for sid, x in nav)
    feats = "、".join(f'<a href="{tag_url("feature", f, root)}">{esc(FEATURES[f]["name"])}</a>' for f in n["features"])
    page = f"""<div class="wrap doc doc-news">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a> / <a href="./">Claude最新情報</a></p>
    <p class="news-date">{esc(n["date"])} の発表</p>
    <h1>{esc(n["title"])}</h1>
    <p class="summary">{esc(n["summary"])}</p>
    <p class="stamp">{esc(n["updated"])} 時点の情報{(" / 関連する機能: " + feats) if feats else ""}</p>
    <ul class="inpage" aria-label="このページの内容">{inpage}</ul>
  </div>
  {body_html}
  {ad_slot()}
  {related_html(n, tips, root)}
  {sister_html()}
  {books_html(n)}
  {sources_html(n)}
  {share_block(n["title"], f"news/{n['slug']}.html")}
  <p style="margin-top:2.5rem"><a href="./">最新情報の一覧にもどる</a></p>
</div>"""
    return layout(n["title"], n["summary"], page, root, f"news/{n['slug']}.html", {"published": n["date"], "modified": n["updated"]})


def guide_card(g, root):
    topic = GUIDE_TOPICS[g["topic"]]["name"]
    chips = (f'<span class="chip chip-g">{esc(topic)}</span><span class="chip">読む目安 約{g["minutes"]}分</span>'
             + "".join(f'<span class="chip chip-f">{esc(FEATURES[f]["name"])}</span>' for f in g["features"]))
    return (
        f'<li class="card card-guide"><p class="card-date">解説 / {esc(topic)}</p>'
        f'<a class="card-title" href="{root}guides/{esc(g["slug"])}.html">{esc(g["title"])}</a>'
        f'<p class="card-sum">{esc(g["summary"])}</p><p class="chips">{chips}</p></li>'
    )


def render_guide(g, tips):
    root = "../"
    body_html, nav = render_body(g["body"], root)
    inpage = "".join(f'<li><a href="#{sid}">{esc(x)}</a></li>' for sid, x in nav)
    feats = "、".join(f'<a href="{tag_url("feature", f, root)}">{esc(FEATURES[f]["name"])}</a>' for f in g["features"])
    rows = [("分類", esc(GUIDE_TOPICS[g["topic"]]["name"])), ("読む目安", f'約{g["minutes"]}分')]
    if feats:
        rows.append(("関連する機能", feats))
    spec = ('<table class="spec"><caption>この解説について</caption><tbody>'
            + "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows) + "</tbody></table>")
    page = f"""<div class="wrap doc doc-guide">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a> / <a href="./">解説</a></p>
    <p class="news-date">解説</p>
    <h1>{esc(g["title"])}</h1>
    <p class="summary">{esc(g["summary"])}</p>
    <p class="stamp">{esc(g["updated"])} 時点の情報</p>
    {spec}
    <ul class="inpage" aria-label="このページの内容">{inpage}</ul>
  </div>
  {body_html}
  {ad_slot()}
  {related_html(g, tips, root)}
  {sister_html()}
  {books_html(g)}
  {sources_html(g)}
  {share_block(g["title"], f"guides/{g['slug']}.html")}
  <p style="margin-top:2.5rem"><a href="./">解説の一覧にもどる</a></p>
</div>"""
    return layout(g["title"], g["summary"], page, root, f"guides/{g['slug']}.html", {"published": g["added"], "modified": g["updated"]})


def render_guides_index(guides):
    gl = sorted_guides(guides)
    secs = ""
    for tid, t in GUIDE_TOPICS.items():
        hit = [g for g in gl if g["topic"] == tid]
        if not hit:
            continue
        secs += (f'<section class="tag-group"><h2>{esc(t["name"])}</h2><p>{esc(t["desc"])}</p>'
                 f'<ul class="card-list">{"".join(guide_card(g, "../") for g in hit)}</ul></section>')
    body = f"""<div class="wrap doc doc-guide">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a></p>
    <h1>解説</h1>
    <p class="summary">機能やツールの違い、しくみ、使い分けを、図と表でじっくり読めるページです。手を動かして試す「活用方法」とは別に、全体像をつかみたいときに使ってください。</p>
  </div>
  {secs}
  {share_block("解説", "guides/")}
  {ad_slot()}
</div>"""
    return layout("解説", "Claudeの機能やツールの違い、しくみ、使い分けを、図と表で詳しく解説します。", body, "../", "guides/")


def sorted_guides(guides):
    return sorted(guides.values(), key=lambda g: (g["added"], g["slug"]), reverse=True)


def sorted_tips(tips):
    order = {q["slug"]: i for i, q in enumerate(QUEUE)}
    return sorted(tips.values(), key=lambda t: (t["added"], -order.get(t["slug"], 999)), reverse=True)


def sorted_news(news):
    return sorted(news.values(), key=lambda n: (n["date"], n["added"]), reverse=True)


def render_index(tips, news, guides):
    tl = sorted_tips(tips)
    nl = sorted_news(news)
    gl = sorted_guides(guides)
    guide_block = ""
    if gl:
        guide_block = ('<section class="latest guides"><h2>解説</h2>'
                       '<p>機能やツールの違いを、図と表でじっくり読めます。</p><ul class="card-list">'
                       + "".join(guide_card(g, "") for g in gl[:3]) + "</ul>"
                       '<p class="more"><a href="guides/">解説の一覧を見る</a></p></section>')
    latest = ""
    if nl:
        latest = ('<section class="latest"><h2>Claude最新情報</h2><ul class="card-list">' + news_card(nl[0], "") + "</ul>"
                  '<p class="more"><a href="news/">最新情報の一覧を見る</a></p></section>')

    def opts(d):
        return "".join(f'<option value="{esc(i)}">{esc(v["name"])}</option>' for i, v in d.items())

    levels = '<button type="button" class="seg-btn is-on" data-level="">すべて</button>' + "".join(
        f'<button type="button" class="seg-btn" data-level="{esc(i)}">{esc(v["name"])}</button>' for i, v in LEVELS.items())
    finder = f"""<section class="finder" aria-label="さがす">
    <div class="seg" role="group" aria-label="難易度">{levels}</div>
    <div class="selects">
      <label>目的 <select id="f-purpose"><option value="">すべて</option>{opts(PURPOSES)}</select></label>
      <label>使う機能 <select id="f-feature"><option value="">すべて</option>{opts(FEATURES)}</select></label>
    </div>
    <label class="search">キーワード <input type="search" id="f-q" placeholder="例: スライド"></label>
    <p id="f-count" class="f-count" aria-live="polite"></p>
  </section>"""
    body = f"""<div class="wrap">
  <div class="cover">
    <h1>{esc(CONFIG["name"])}</h1>
    <p class="sub">{esc(CONFIG["subtitle"])}</p>
    <p class="lead">Claudeには、使い始めたときには気づきにくい使い方がたくさんあります。ここでは、1つの使い方を、手順、そのまま貼って使えるプロンプト、つまずきやすい点まで、同じ形式で整理します。まず1つ、手を動かして試してみてください。</p>
    <p class="quick"><a href="cheatsheet.html">プロンプト10個の早見表</a><a href="news/">Claude最新情報</a><a href="guides/">解説</a></p>
  </div>
  <section class="toc">
    <h2>活用方法の一覧</h2>
    <details class="howto">
      <summary>探し方の説明を見る</summary>
      <dl>
        <dt>難易度</dt><dd>{level_chip("beginner")} 画面の操作だけで試せます。{level_chip("intermediate")} 設定や、複数の機能の組み合わせが要ります。</dd>
        <dt>目的</dt><dd>調べる、書く、作る、自動化する、整理する、学ぶ、のどれにあたるかです。</dd>
        <dt>使う機能</dt><dd>Projects、Artifacts、定期タスクなど、使う機能で絞れます。</dd>
        <dt>解説</dt><dd>手を動かす前に、機能やツールの違いを図と表で読みたいときのページです。</dd>
      </dl>
    </details>
    {finder}
    <ul class="card-list" id="tip-list">{"".join(card(t, "") for t in tl)}</ul>
    <p class="f-empty" id="f-empty" hidden>条件に合うものがありません。条件をゆるめてみてください。</p>
  </section>
  {latest}
  {guide_block}
  {share_block(CONFIG["name"], "")}
  {ad_slot()}
</div>"""
    return layout(CONFIG["name"], CONFIG["description"], body, "", "", full_title=CONFIG.get("home_title"))


CHEAT = ["summarize-long-text", "email-draft-with-purpose", "tone-rewrite", "meeting-notes-to-actions", "ask-claude-to-ask-you",
         "explain-like-teacher", "web-search-fact-check", "quiz-yourself", "trip-plan-by-day", "image-read-receipt"]


def render_cheatsheet(tips):
    items = []
    for i, slug in enumerate([c for c in CHEAT if c in tips], 1):
        t = tips[slug]
        text = first_prompt(t["body"])
        if not text:
            continue
        code, n = mark_placeholders(text)
        bar = f"色のついた{n}か所を書き換えてから使います" if n else "そのまま貼って使えます"
        items.append(f'<section class="cheat"><h2>{i}. {esc(t["title"])}</h2>'
                     f'<div class="prompt"><div class="prompt-bar"><span>{bar}</span>'
                     f'<button type="button" class="copy" data-copy>コピー</button></div><pre><code>{code}</code></pre></div>'
                     f'<p class="more"><a href="tips/{esc(slug)}.html">手順とつまずきやすい点を読む</a></p></section>')
    title = f"すぐ試せるプロンプト{len(items)}個の早見表"
    desc = f"Claudeにそのまま貼って試せるプロンプトを{len(items)}個、1ページにまとめました。要約、メール、言い換え、やることの整理、調べものなど。印刷や保存にも使えます。"
    page = f"""<div class="wrap article cheatsheet">
  <div class="cover"><h1>{title}</h1>
  <p class="summary">初心者向けの活用方法から、プロンプトだけを1ページにまとめました。色のついた部分があるときは、自分の内容に書き換えて使います。</p>
  <p class="noprint"><button type="button" class="copy" onclick="window.print()">このページを印刷する</button></p></div>
  {"".join(items)}
  <p class="noprint" style="margin-top:2.5rem"><a href="./">ホームにもどる</a></p>
</div>"""
    return layout(title, desc, page, "", "cheatsheet.html")


def render_news_index(news):
    nl = sorted_news(news)
    body = f"""<div class="wrap doc doc-news">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a></p>
    <h1>Claude最新情報</h1>
    <p class="summary">Claudeの新しい機能やモデルの発表を、1つずつ取り上げます。何が変わったか、どう試せるか、注意点は何かを、公式の情報をもとにまとめます。</p>
  </div>
  <ul class="card-list">{"".join(news_card(n, "../") for n in nl)}</ul>
  {share_block("Claude最新情報", "news/")}
  {ad_slot()}
</div>"""
    return layout("Claude最新情報", "Claudeの新しい機能やモデルの発表を、公式の情報をもとに、活用方法つきでまとめます。", body, "../", "news/")


def tag_defs():
    out = []
    for i, v in LEVELS.items():
        out.append(("level", i, v["name"], v["desc"], lambda t, i=i: t["level"] == i))
    for i, v in PURPOSES.items():
        out.append(("purpose", i, v["name"], v["desc"], lambda t, i=i: t["purpose"] == i))
    for i, v in FEATURES.items():
        out.append(("feature", i, v["name"], v["desc"], lambda t, i=i: i in t["features"]))
    return out


KIND_NAME = {"level": "難易度", "purpose": "目的", "feature": "使う機能"}


def render_tags(tips, news, guides):
    tl = sorted_tips(tips)
    nl = sorted_news(news)
    gl = sorted_guides(guides)
    pages = {}
    groups = {"level": [], "purpose": [], "feature": []}
    for kind, tid, name, desc, pred in tag_defs():
        hit = [t for t in tl if pred(t)]
        news_hit = [n for n in nl if kind == "feature" and tid in n["features"]]
        guide_hit = [g for g in gl if kind == "feature" and tid in g["features"]]
        groups[kind].append((tid, name, desc, len(hit) + len(news_hit) + len(guide_hit)))
        if not hit and not news_hit and not guide_hit:
            continue
        lst = '<ul class="card-list">' + "".join(card(t, "../") for t in hit) + "</ul>" if hit else ""
        nws = ('<h2>関連する最新情報</h2><ul class="card-list">' + "".join(news_card(n, "../") for n in news_hit) + "</ul>") if news_hit else ""
        gds = ('<h2>関連する解説</h2><ul class="card-list">' + "".join(guide_card(g, "../") for g in guide_hit) + "</ul>") if guide_hit else ""
        body = f"""<div class="wrap doc">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a> / <a href="./">タグでさがす</a></p>
    <p class="news-date">{KIND_NAME[kind]}</p>
    <h1>{esc(name)}</h1>
    <p class="summary">{esc(desc)}。{len(hit)}件の活用方法があります。</p>
  </div>
  {lst}
  {gds}
  {nws}
  {ad_slot()}
</div>"""
        pages[f"{kind}-{tid}.html"] = layout(f"タグ: {name}", f"{KIND_NAME[kind]}「{name}」の活用方法の一覧。", body, "../", f"tags/{kind}-{tid}.html")
    sections = ""
    for kind in ("level", "purpose", "feature"):
        li = "".join(
            f'<li><a href="{kind}-{tid}.html">{esc(name)}</a> <span class="count">{cnt}件</span><span class="tag-desc">{esc(desc)}</span></li>'
            for tid, name, desc, cnt in groups[kind] if cnt)
        sections += f'<section class="tag-group"><h2>{KIND_NAME[kind]}</h2><ul class="tag-list">{li}</ul></section>'
    index = f"""<div class="wrap doc">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a></p>
    <h1>タグでさがす</h1>
    <p class="summary">難易度、目的、使う機能の3つの軸で、活用方法を探せます。</p>
  </div>
  {sections}
  {ad_slot()}
</div>"""
    pages["index.html"] = layout("タグでさがす", "難易度、目的、使う機能の3つの軸で、Claudeの活用方法を探せます。", index, "../", "tags/")
    return pages


def render_glossary():
    cats = []
    for g in GLOSSARY:
        if g["category"] not in cats:
            cats.append(g["category"])
    jump = "".join(f'<li><a href="#cat{i}">{esc(c)}</a></li>' for i, c in enumerate(cats))
    secs = []
    for i, c in enumerate(cats):
        items = "".join(
            f'<div class="term-item" id="term-{g["id"]}"><dt>{esc(g["term"])}'
            + (f'<span class="reading">{esc(g["reading"])}</span>' if g.get("reading") else "")
            + f'</dt><dd>{inline(g["explain"])}</dd></div>'
            for g in GLOSSARY if g["category"] == c
        )
        secs.append(f'<section id="cat{i}"><h2>{esc(c)}</h2><dl class="terms">{items}</dl></section>')
    page = f"""<div class="wrap doc">
  <div class="doc-head">
    <p class="crumb"><a href="../">ホーム</a></p>
    <h1>用語解説</h1>
    <p class="summary">各ページに出てくる言葉を、やさしく説明します。各ページの言葉から、ここへ移れます。</p>
    <ul class="inpage" aria-label="分類">{jump}</ul>
  </div>
  {"".join(secs)}
  <p style="margin-top:2.5rem"><a href="../">ホームにもどる</a></p>
</div>"""
    return layout("用語解説", "Claudeの活用方法のページに出てくる言葉を、やさしく説明します。", page, "../", "glossary/")


def render_sitemap(tips, news, guides, tag_pages):
    base = CONFIG["base_url"]
    def items_of(coll):
        return coll.values() if isinstance(coll, dict) else coll
    def mod(coll, slug):
        it = coll[slug] if isinstance(coll, dict) else next((x for x in coll if x.get("slug") == slug), None)
        return str(it.get("updated", "")) if it else ""
    dates = [str(x.get("updated", "")) for c in (tips, news, guides) for x in items_of(c) if isinstance(x, dict)]
    latest = max([d for d in dates if d] or [""])
    urls = [(base, latest), (base + "guides/", latest), (base + "news/", latest), (base + "tags/", latest), (base + "glossary/", latest), (base + "cheatsheet.html", latest)]
    urls += [(f"{base}guides/{s}.html", mod(guides, s)) for s in guides_slugs(guides)]
    urls += [(f"{base}tips/{s}.html", mod(tips, s)) for s in guides_slugs(tips)]
    urls += [(f"{base}news/{s}.html", mod(news, s)) for s in guides_slugs(news)]
    urls += [(f"{base}tags/{p}", latest) for p in tag_pages if p != "index.html"]
    body = "".join(f"<url><loc>{esc(u)}</loc>" + (f"<lastmod>{esc(d)}</lastmod>" if d else "") + "</url>" for u, d in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def guides_slugs(coll):
    return list(coll) if isinstance(coll, dict) else [x["slug"] for x in coll]


def write_dir(directory, files):
    directory.mkdir(parents=True, exist_ok=True)
    for old in directory.glob("*.html"):
        if old.name not in files:
            old.unlink()
    for name, content in files.items():
        (directory / name).write_text(content, encoding="utf-8")


def build():
    tips = load_dir(TIPS_DIR, TIP_REQUIRED, "tip")
    news = load_dir(NEWS_DIR, NEWS_REQUIRED, "news")
    guides = load_dir(GUIDES_DIR, GUIDE_REQUIRED, "guide")
    known = {q["slug"] for q in QUEUE}
    for s in tips:
        if s not in known:
            print(f"注意: {s} は data/queue.json にありません(一覧には出ますが、掲載予定とは対応しません)")
    for m in list(tips.values()) + list(news.values()) + list(guides.values()):
        for s in m["next"]:
            if s not in tips:
                raise SystemExit(f"{m['slug']}: next に指定した {s} が content/tips/ にありません")
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "index.html").write_text(render_index(tips, news, guides), encoding="utf-8")
    (DOCS / "cheatsheet.html").write_text(render_cheatsheet(tips), encoding="utf-8")
    write_dir(DOCS / "tips", {f"{s}.html": render_tip(t, tips) for s, t in tips.items()})
    write_dir(DOCS / "news", {"index.html": render_news_index(news), **{f"{s}.html": render_news(n, tips) for s, n in news.items()}})
    write_dir(DOCS / "guides", {"index.html": render_guides_index(guides), **{f"{s}.html": render_guide(g, tips) for s, g in guides.items()}})
    tag_pages = render_tags(tips, news, guides)
    write_dir(DOCS / "tags", tag_pages)
    write_dir(DOCS / "glossary", {"index.html": render_glossary()})
    (DOCS / "sitemap.xml").write_text(render_sitemap(tips, news, guides, tag_pages), encoding="utf-8")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['base_url']}sitemap.xml\n", encoding="utf-8")
    print(f"生成しました: 活用方法 {len(tips)}件 / 解説 {len(guides)}件 / 最新情報 {len(news)}件 / タグページ {len(tag_pages)}件")


def first_prompt(body):
    for kind, c in to_blocks(body):
        if kind == "fig" and c[0].startswith("prompt"):
            return "\n".join(c[1]).strip("\n")
    return ""


def archive_json():
    tips = load_dir(TIPS_DIR, TIP_REQUIRED, "tip")
    news = load_dir(NEWS_DIR, NEWS_REQUIRED, "news")
    base = CONFIG["base_url"]
    guides = load_dir(GUIDES_DIR, GUIDE_REQUIRED, "guide")
    out = {"site": {"name": CONFIG["name"], "url": base}, "tips": [], "news": [], "guides": []}
    for g in sorted_guides(guides):
        out["guides"].append({
            "slug": g["slug"], "title": g["title"], "summary": g["summary"], "topic": g["topic"],
            "minutes": g["minutes"], "features": g["features"], "added": g["added"], "updated": g["updated"],
            "url": f"{base}guides/{g['slug']}.html"})
    for t in sorted_tips(tips):
        out["tips"].append({
            "slug": t["slug"], "title": t["title"], "summary": t["summary"], "level": t["level"],
            "minutes": t["minutes"], "purpose": t["purpose"], "features": t["features"], "output": t["output"],
            "added": t["added"], "updated": t["updated"], "prompt": first_prompt(t["body"]), "url": f"{base}tips/{t['slug']}.html"})
    for n in sorted_news(news):
        out["news"].append({
            "slug": n["slug"], "title": n["title"], "summary": n["summary"], "date": n["date"],
            "features": n["features"], "added": n["added"], "updated": n["updated"], "prompt": first_prompt(n["body"]), "url": f"{base}news/{n['slug']}.html"})
    out["levels"] = {k: v["name"] for k, v in LEVELS.items()}
    out["purposes"] = {k: v["name"] for k, v in PURPOSES.items()}
    out["features"] = {k: v["name"] for k, v in FEATURES.items()}
    print(json.dumps(out, ensure_ascii=False, indent=2))


def show_next():
    done = {p.stem for p in TIPS_DIR.glob("*.md")}
    for q in QUEUE:
        if q["slug"] not in done:
            print(f'{q["slug"]}\t{q["title"]}\t{q["level"]}\t{q["purpose"]}\t{",".join(q["features"])}')
            return
    print("追加予定の活用方法はすべて掲載済みです。data/queue.json に候補を足してください。")


if __name__ == "__main__":
    if "--next" in sys.argv:
        show_next()
    elif "--archive-json" in sys.argv:
        archive_json()
    else:
        build()
