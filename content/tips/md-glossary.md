---
title: glossary.mdに、言葉の表記をそろえて、ぶれをなくす
level: beginner
minutes: 10
purpose: write
features: chat, projects
output: 言葉の表記表(glossary.md)
summary: 「活用方法」と「使い方」のように、ぶれやすい言葉を、glossary.mdで統一する方法です。
added: 2026-10-30
updated: 2026-10-30
next: md-style
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

同じものを、ある記事では「使い方」、別の記事では「活用方法」と書くと、読む人が戸惑います。glossary.mdは、言葉の表記を決めて並べた表です。

## ねらい

- 表記のぶれを減らします。
- Claudeに文章を直してもらうとき、基準を渡せます。
- 用語の意味も、1行で残せます。

## 準備するもの

- ぶれやすい言葉を5〜10個。
- それぞれの、採用する表記と、避ける表記。

## 手順

:::flow 図: glossary.mdを作って、点検に使うまで
ぶれた言葉を集める | 過去の文章から、探す
採用する表記を決める | 1つに決めて、避ける表記も書く
表にする | 「採用 | 避ける | 意味」の3列
点検させる | 下のプロンプトで、文章の表記を確かめる
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

このmdをClaudeに渡す方法は2つです。1つ目は、中身をチャットに貼ること。2つ目は、Projectsの「プロジェクトの指示」に貼るか、ナレッジにファイルとして入れることです。公式ヘルプでは、Projectの指示は「Set project instructions」から保存し、そのProjectのすべてのチャットで使われると説明されています。ナレッジは、プロジェクト画面の右側から「+」で追加します。

## そのまま使えるプロンプト

:::prompt 文章から、表記のぶれを探す
次の文章を読んで、表記がぶれている言葉(同じものを別の言い方で書いている箇所)を、すべて挙げてください。それぞれ、どちらかに統一する案を出してください。文章は、まだ直さないでください。

(ここに文章を貼る)
:::

:::prompt glossary.mdに沿って直す
次のglossary.mdの表記に合わせて、下の文章を直してください。直した箇所だけを、一覧にして最後に付けてください。

【glossary.md】
(ここに貼る)

【文章】
(ここに貼る)
:::

## うまくいかないとき

- **直しすぎるとき**: 「表記だけを直し、文の意味や構成は変えない」と書き添えます。
- **専門用語の意味まで変わるとき**: 意味の欄に、1行の定義を書きます。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
