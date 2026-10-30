---
title: README.mdに、構成と手順を書いて、Claudeに読ませる
level: beginner
minutes: 15
purpose: organize
features: chat, files, claude-code
output: 作業の入口になるREADME.md
summary: README.mdに、構成・手順・書式を書いておくと、人にもClaudeにも、作業の入口になります。書く項目と、読ませ方をまとめます。
added: 2026-10-30
updated: 2026-10-30
next: md-claude-md
sources:
- Claude Code ドキュメント「How Claude remembers your project」(CLAUDE.mdの置き場所、読み込み、書き方。2026年10月30日に確認) | https://code.claude.com/docs/en/memory
- Claude ヘルプセンター「Upload files to Claude」(対応するファイル形式、チャットの上限。2026年10月30日に確認) | https://support.claude.com/en/articles/8241126-uploading-files-to-claude
---

README.mdは、「このフォルダ(リポジトリ)は何で、どう使うか」を書く入口のファイルです。Claudeに作業を頼むときも、READMEがあると、前提の説明が短くなります。

## ねらい

- 初めて開く人にも、Claudeにも、全体が分かるようにします。
- 作り方・直し方の手順を、1か所に残します。
- 約束を書き込み、CLAUDE.mdから参照させます。

## 準備するもの

- 何のためのフォルダかを、1〜2文。
- 構成(どのフォルダに何があるか)、よく使うコマンド、書式の決まり。

## 手順

:::flow 図: README.mdを作って、Claudeに読ませるまで
1〜2文で目的を書く | 最初に置く
構成を表にする | パスと内容を1行ずつ
手順を書く | 作り方、確認の仕方、公開の仕方
Claudeに読ませる | チャットに貼る。Claude Codeなら、CLAUDE.mdに「@README」と書くと取り込める(公式の例)
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

## そのまま使えるプロンプト

:::prompt READMEの下書きを作る
次のフォルダの説明をもとに、README.mdの下書きを作ってください。見出しは「目的」「構成」「手順」「書式の決まり」にします。手順は、番号つきで書いてください。分からない部分は、推測せず「(要確認)」と書いてください。

(ここにフォルダの説明を貼る)
:::

:::prompt READMEを読んで答えさせる
次のREADME.mdを読んで、このフォルダで新しい文書を1つ足すときの手順を、5行以内で教えてください。READMEに書かれていないことは、「書かれていません」と答えてください。

(ここにREADME.mdを貼る)
:::

## うまくいかないとき

- **READMEが長くなったとき**: 約束は rules.md、決めた理由は decisions.md に分けます。
- **古くなったとき**: 手順を変えたら、同じ日にREADMEも直します。
- **mdファイルを添付できないとき**: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
