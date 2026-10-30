---
title: style.mdに、文体の決まりを書いて、文章の調子をそろえる
level: beginner
minutes: 15
purpose: write
features: chat, projects
output: 文体の決まり(style.md)
summary: 文の長さ、使わない言葉、見出しの型を、style.mdに書いて、Claudeの文章の調子をそろえる方法です。
added: 2026-10-30
updated: 2026-10-30
next: md-rules
books:
- はじめての生成AI Claude「超」活用術 | ソーテック社 | 978-4-8007-2163-1
- 今すぐ使えるかんたんEx Claude 仕事術&時短技 | リンクアップ(技術評論社) | 978-4-297-15838-5
- これからのAI×業務改善本格講座 Claude AIで超効率資料作成・情報整理 | 秀和システム新社 | 978-4-7980-7738-3
sources:
- Claude ヘルプセンター「How can I create and manage projects?」(Projectの指示とナレッジの設定。2026年10月30日に確認) | https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude ヘルプセンター「Upload files to Claude」(対応するファイル形式、チャットの上限。2026年10月30日に確認) | https://support.claude.com/en/articles/8241126-uploading-files-to-claude
- 丸善ジュンク堂書店「はじめての生成AI Claude「超」活用術」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784800721631
- 丸善ジュンク堂書店「Claude 仕事術&時短技」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784297158385
- 丸善ジュンク堂書店「Claude AIで超効率資料作成・情報整理」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784798077383
---

何本も文章を書くと、調子がばらつきます。style.mdは、文体の決まりだけを集めたファイルです。rules.mdが「やってよいこと・いけないこと」なら、style.mdは「どう書くか」です。

## ねらい

- 文章の調子をそろえます。
- 直してもらうとき、基準を渡せます。
- 自分の文章の癖に気づけます。

## 準備するもの

- 手本にしたい自分の文章を1〜2本。
- 文体の決まりを5つほど(文の長さ、「です・ます」、見出しの型など)。

## 手順

:::flow 図: style.mdを作って、使うまで
手本の文章を渡す | 自分が書いた、気に入っている文章を1〜2本
決まりを書き出してもらう | 下のプロンプトで下書きを作る
自分で直す | 合っていないものを消す
文章を直す依頼に使う | 毎回、style.mdを添える
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

このmdをClaudeに渡す方法は2つです。1つ目は、中身をチャットに貼ること。2つ目は、Projectsの「プロジェクトの指示」に貼るか、ナレッジにファイルとして入れることです。公式ヘルプでは、Projectの指示は「Set project instructions」から保存し、そのProjectのすべてのチャットで使われると説明されています。ナレッジは、プロジェクト画面の右側から「+」で追加します。

## そのまま使えるプロンプト

:::prompt 手本から文体の決まりを書き出す
次の文章は、私が書いたものです。この文章の文体の特徴を、style.mdの形で、5つ以内の箇条書きにしてください。それぞれに、文章からの短い例を添えてください。文章にない特徴は、書かないでください。

(ここに手本の文章を貼る)
:::

:::prompt 決まりに沿って直す
次のstyle.mdに沿って、下の文章を直してください。意味は変えないでください。直した箇所と、その理由を、最後に3つ以内で書いてください。

【style.md】
(ここに貼る)

【文章】
(ここに貼る)
:::

## うまくいかないとき

- **決まりが多すぎて守られないとき**: 5つ以内に絞ります。
- **手本の癖まで真似されるとき**: 「直したい癖」も、決まりとして書きます。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
