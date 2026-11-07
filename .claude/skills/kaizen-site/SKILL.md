---
name: kaizen-site
description: あんなことこんなことClaudeの「改善の1周」で、このサイトだけに当てはまる部分(読者像、判断の観点、確かめ方)。共通の手順は TakahiroUkai/site-ops の kaizen-loop スキルにある。
---

# 改善の1周(あんなことこんなことClaudeだけの部分)

共通の手順(`TakahiroUkai/site-ops` の `.claude/skills/kaizen-loop/SKILL.md`)と一緒に使う。

## 基本

- 項目の接頭辞: `AK`(司令塔の `site` は `anna`)
- 既定ブランチ: **`master`**。公開URL: https://takahiroukai.github.io/anna-konna-claude/
- 改善の順番: 2番目(稼ぎのトリセツ → あんなことこんなことClaude → 机タイム素材集 → 注目銘柄メモの順に、実行のたびに次へ進む)

## ユーザー役の読者像

`style.md` の「想定読者」の初心者と中級者の2人を順に演じる。スマホ幅で、トップページ → タグや難易度で探す → 活用方法を1つ読んでプロンプトをコピーする → 最新情報・解説ページ、の順に使い、「自分に合う活用方法にたどり着けるか」「そのまま試せるか」を確かめる。

## 事業推進役の観点(共通の観点に加えて)

目標への効き方を第一に見る(下の「目標の測り方」)。そのうえで:

- 探したい活用方法に、少ない操作でたどり着けるか(タグ、難易度、目的)。
- プロンプトのコピーや手順が、スマホでも使いやすいか。
- ほかのサイトへの自然な導線になるか。

## 目標の測り方

- 目標の立て方・確かめ方は `TakahiroUkai/site-ops` の `docs/GOALS.md`、目標そのものは司令塔の `goals` にある。
- アクセス数: `TakahiroUkai/stock-memo2` の `data/analytics.json` の `key: "claude"`(path `/anna-konna-claude/`)。キーが `anna` ではないことに注意。
- 読み進めてもらう段では、`top_pages` のうち活用方法(`/anna-konna-claude/tips/`)、最新情報(`/news/`)、解説(`/guides/`)、用語解説(`/glossary/`)の閲覧を見る。
- プロンプトのコピーは計測していない。
- 目標に効きやすい打ち手の例: 記事の題名・説明文(検索結果に出る文)、sitemap、共有されたときの見え方、タグ・難易度からの導線、関連する活用方法への導線、稼ぎのトリセツ・注目銘柄メモへの導線。

## 直してよい範囲

- `build.py` のページの組み立て、CSS、一覧・タグの見せ方、既存の記事の分かりにくい文。
- 直さない: `config/site.json` の広告・アフィリエイト、`data/queue.json` の順番、`RULES.md` と `style.md`(変えたほうがよいときは「要確認」の項目にする)。古い仕様が書かれた記事を直すときは、公式で確かめてから直す。

## 確かめ方

1. `python3 build.py`
2. `python3 check.py --visual` で ERROR が 0 件(WARN も読む)。
3. 変えたページを、スマホ幅(iPhone 13 相当)のスクリーンショットで見て、崩れがないこと。
