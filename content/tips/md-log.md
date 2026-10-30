---
title: log.mdに、やったことを日付つきで残して、続きから始める
level: beginner
minutes: 10
purpose: organize
features: chat, projects
output: 日付つきの作業ログ(log.md)
summary: log.mdに、毎回の作業を数行ずつ残すと、翌日の続きがすぐ始められます。書く項目と、Claudeの使い方をまとめます。
added: 2026-10-30
updated: 2026-10-30
next: md-decisions
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

作業を中断すると、「どこまでやったか」を思い出す時間がかかります。log.mdは、作業のたびに、日付つきで数行を足していく記録です。Claudeに渡せば、続きから始めやすくなります。

## ねらい

- 中断した作業を、すぐ再開できるようにします。
- 同じ題材を二重に作る失敗を防ぎます。
- 振り返りの材料にします。

## 準備するもの

- 作業の終わりに、3行ほど書く時間。
- 1件につき、日付、やったこと、次にやること。

## 手順

:::flow 図: log.mdを作って、毎回足すまで
作業の終わりに書く | 「日付 / やったこと / 次にやること」
新しいものを上に足す | 最新が先頭に来る
次の作業の前に渡す | 直近の5件を貼る
重複を確かめる | 同じ題材がないかを、Claudeに確かめさせる
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

このmdをClaudeに渡す方法は2つです。1つ目は、中身をチャットに貼ること。2つ目は、Projectsの「プロジェクトの指示」に貼るか、ナレッジにファイルとして入れることです。公式ヘルプでは、Projectの指示は「Set project instructions」から保存し、そのProjectのすべてのチャットで使われると説明されています。ナレッジは、プロジェクト画面の右側から「+」で追加します。

## そのまま使えるプロンプト

:::prompt 作業メモをログの形にする
次の作業メモを、log.mdの1件にしてください。形は「日付 / やったこと / 次にやること」で、全体を3行以内にしてください。書かれていないことは補わないでください。

(ここにメモを貼る)
:::

:::prompt 続きを始める
次のlog.mdを読んで、今日の作業の最初の1歩を、1つ提案してください。すでにやったことと重ならないか、log.mdに照らして確かめてから答えてください。

(ここにlog.mdを貼る)
:::

## うまくいかないとき

- **書くのを忘れるとき**: 作業の最後に、Claudeに「今日のログを書いて」と頼みます。事実は自分で確かめてから足します。
- **ログが長くなったとき**: 直近の5〜10件だけを渡します。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
