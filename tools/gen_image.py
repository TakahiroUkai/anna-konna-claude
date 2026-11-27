#!/usr/bin/env python3
"""画像を生成して docs/img/gen/ に保存する(Cloudflare Workers AI の FLUX.1 schnell)。

使い方:
  python3 tools/gen_image.py            # data/image-prompts.json の、まだ画像がないものだけ生成する
  python3 tools/gen_image.py --force    # すべて作り直す

必要な環境変数(GitHub Actions では Secrets から渡す。値は画面にもファイルにも書き出さない):
  CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN
Python の標準ライブラリだけで動く。
"""
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "data/image-prompts.json"
OUT_DIR = ROOT / "docs/img/gen"
RESULTS = ROOT / "data/image-results.json"
MODEL = "@cf/black-forest-labs/flux-1-schnell"
MAX_PER_RUN = 8  # 1回の実行で作る上限。無料枠(1日10,000ニューロン)を使いきらないための安全装置


def jpeg_size(data):
    """JPEG の幅と高さを、ファイルの先頭の情報から読む。"""
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            return int.from_bytes(data[i + 7:i + 9], "big"), int.from_bytes(data[i + 5:i + 7], "big")
        i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    return None, None


def estimate_neurons(width, height, steps):
    """公開されている料金表(512x512のタイルごとに4.80、ステップごとに9.60ニューロン)による見積もり。"""
    tiles = -(-width // 512) * -(-height // 512)
    return round(tiles * 4.80 + steps * 9.60, 1)


def generate(account, token, item):
    url = f"https://api.cloudflare.com/client/v4/accounts/{account}/ai/run/{MODEL}"
    # seed(乱数の種)は、公式の例にあるが、実際に送ると「許可されていない項目」として断られたため送らない
    body = {"prompt": item["prompt"], "steps": item.get("steps", 4)}
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as res:
        ctype = res.headers.get("Content-Type", "")
        raw = res.read()
    if ctype.startswith("image/"):
        return raw
    data = json.loads(raw)
    image = (data.get("result") or {}).get("image") or data.get("image")
    if not image:
        raise RuntimeError("応答に画像がありません: " + ", ".join(str(e) for e in data.get("errors", [])))
    return base64.b64decode(image)


def main():
    force = "--force" in sys.argv
    account = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
    token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    items = json.loads(PROMPTS.read_text(encoding="utf-8"))
    results = json.loads(RESULTS.read_text(encoding="utf-8")) if RESULTS.exists() else {}
    todo = [it for it in items if force or not (OUT_DIR / (it["id"] + ".jpg")).exists()]
    if not todo:
        print("作る画像はありません(すべて生成済みです)")
        return 0
    if not account or not token:
        print("エラー: CLOUDFLARE_ACCOUNT_ID と CLOUDFLARE_API_TOKEN が設定されていません(GitHub の Secrets を確認してください)")
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    failed = 0
    for n, it in enumerate(todo[:MAX_PER_RUN], 1):
        start = time.time()
        try:
            img = generate(account, token, it)
        except urllib.error.HTTPError as e:
            # 応答の本文には、原因のメッセージだけが入っている(トークンは含まれない)
            print(f"[{n}/{len(todo)}] {it['id']}: 失敗 HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")
            failed += 1
            continue
        except Exception as e:  # noqa: BLE001
            print(f"[{n}/{len(todo)}] {it['id']}: 失敗 {type(e).__name__}: {e}")
            failed += 1
            continue
        (OUT_DIR / (it["id"] + ".jpg")).write_bytes(img)
        w, h = jpeg_size(img)
        steps = it.get("steps", 4)
        results[it["id"]] = {
            "prompt": it["prompt"], "steps": steps,
            "width": w, "height": h, "bytes": len(img),
            "seconds": round(time.time() - start, 1),
            "estimated_neurons": estimate_neurons(w, h, steps) if w and h else None,
        }
        print(f"[{n}/{len(todo)}] {it['id']}: 成功 {w}x{h}px {len(img)//1024}KB {results[it['id']]['seconds']}秒 steps={steps}")
        RESULTS.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        time.sleep(1)
    if len(todo) > MAX_PER_RUN:
        print(f"上限({MAX_PER_RUN}枚)に達したので、残り{len(todo) - MAX_PER_RUN}枚は次回に回します")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
