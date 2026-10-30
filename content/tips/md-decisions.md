---
title: decisions.mdに、決めた理由を残して、後で迷わないようにする
level: beginner
minutes: 10
purpose: organize
features: chat, projects
output: 決めたことと理由の記録(decisions.md)
summary: 「なぜそう決めたか」を、decisions.mdに1行ずつ残す方法です。後から見直すとき、Claudeにも前提を渡せます。
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

決めたことは覚えていても、理由は忘れがちです。理由を忘れると、同じ議論をやり直したり、Claudeに別の案を勧められて迷ったりします。decisions.mdは、決めた内容と理由を、短く残すためのファイルです。

## ねらい

- 同じことを、何度も決め直さないようにします。
- Claudeに提案を頼むとき、決めたことを前提として渡します。
- やめたことも、理由つきで残します。

## 準備するもの

- 最近決めたことを3つほど。
- 1件につき、日付、決めたこと、理由、(あれば)やめた案。

## 手順

:::flow 図: decisions.mdを書いて、使うまで
1件ずつ書く | 「日付 / 決めたこと / 理由 / やめた案」の4行
新しいものを上に足す | 最新が先に目に入るように
相談のときに渡す | 提案を頼む前に貼る
見直す | 前提が変わったら、新しい決定として足す(古いものは消さない)
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

このmdをClaudeに渡す方法は2つです。1つ目は、中身をチャットに貼ること。2つ目は、Projectsの「プロジェクトの指示」に貼るか、ナレッジにファイルとして入れることです。公式ヘルプでは、Projectの指示は「Set project instructions」から保存し、そのProjectのすべてのチャットで使われると説明されています。ナレッジは、プロジェクト画面の右側から「+」で追加します。

## そのまま使えるプロンプト

:::prompt 決定を記録の形に直す
次のメモを、decisions.mdの1件にしてください。形は「日付 / 決めたこと / 理由 / やめた案」です。メモに書かれていない理由は、補わず「理由は未記入」としてください。

(ここにメモを貼る)
:::

:::prompt 決定を前提に相談する
次のdecisions.mdで決めたことを前提にして、次の質問に答えてください。決めたことと食い違う提案をする場合は、その点を最初に書いてください。

【decisions.md】
(ここに貼る)

【質問】
(ここに書く)
:::

## うまくいかないとき

- **理由が思い出せないとき**: 無理に作らず、「理由は未記入」と残します。
- **件数が増えたとき**: 古いものは別ファイルに移し、最近の10件だけを渡します。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
