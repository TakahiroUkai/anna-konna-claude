---
name: kaizen-site
description: あんなことこんなことClaudeの「改善の1周」で、このサイトだけに当てはまる部分(読者像、判断の観点、確かめ方)。共通の手順は TakahiroUkai/site-ops の kaizen-loop スキルにある。
---

# 改善の1周(あんなことこんなことClaudeだけの部分)

共通の手順(`TakahiroUkai/site-ops` の `.claude/skills/kaizen-loop/SKILL.md`)と一緒に使う。

## 基本

- 項目の接頭辞: `AK`(司令塔の `site` は `anna`)
- 既定ブランチ: **`master`**。公開URL: https://takahiroukai.github.io/anna-konna-claude/
- 改善の曜日: 火曜

## ユーザー役の読者像

`style.md` の「想定読者」の初心者と中級者の2人を順に演じる。スマホ幅で、トップページ → タグや難易度で探す → 活用方法を1つ読んでプロンプトをコピーする → 最新情報・解説ページ、の順に使い、「自分に合う活用方法にたどり着けるか」「そのまま試せるか」を確かめる。

## 事業推進役の観点(共通の観点に加えて)

- 探したい活用方法に、少ない操作でたどり着けるか(タグ、難易度、目的)。
- プロンプトのコピーや手順が、スマホでも使いやすいか。
- ほかのサイトへの自然な導線になるか。

## 直してよい範囲

- `build.py` のページの組み立て、CSS、一覧・タグの見せ方、既存の記事の分かりにくい文。
- 直さない: `config/site.json` の広告・アフィリエイト、`data/queue.json` の順番、`RULES.md` と `style.md`(変えたほうがよいときは「要確認」の項目にする)。古い仕様が書かれた記事を直すときは、公式で確かめてから直す。

## 確かめ方

1. `python3 build.py`
2. `python3 check.py --visual` で ERROR が 0 件(WARN も読む)。
3. 変えたページを、スマホ幅(iPhone 13 相当)のスクリーンショットで見て、崩れがないこと。
