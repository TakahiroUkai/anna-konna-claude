---
title: sources.mdに、確認済みの出典をまとめて、毎回の調べ直しをなくす
level: beginner
minutes: 10
purpose: research
features: chat, files, search
output: 確認済みの出典の一覧(sources.md)
summary: よく使う公式ページや、確認した書誌情報を、sources.mdにまとめて、確認した日つきで残す方法です。
added: 2026-10-30
updated: 2026-10-30
next: summarize-long-text
sources:
- Claude ヘルプセンター「Upload files to Claude」(対応するファイル形式、チャットの上限。2026年10月30日に確認) | https://support.claude.com/en/articles/8241126-uploading-files-to-claude
- Claude ヘルプセンター「How can I create and manage projects?」(Projectの指示とナレッジの設定。2026年10月30日に確認) | https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
---

調べたことの出典は、あとで探し直すと意外に手間がかかります。sources.mdは、確認済みのページを、確認日つきで残しておくファイルです。書くときに、Claudeに見せて、「この出典に書かれている範囲で」と頼めます。

## ねらい

- 出典探しの時間を減らします。
- 確認した日と、確認した内容を、一緒に残します。
- 確認できなかったことを、「確認できませんでした」と書いて残します。

## 準備するもの

- よく使う公式ページや、書誌情報。
- 1件につき、ページの題名、URL、確認日、何の確認に使ったか。

## 手順

:::flow 図: sources.mdを作って、使うまで
出典を1件ずつ書く | 「題名 / URL / 確認日 / 確認した内容」
確認できなかったことも書く | 「確認できませんでした」と残す
文章を書くとき渡す | 「この範囲で書いて」と添える
定期的に見直す | ページは変わるので、確認日を更新する
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

このmdをClaudeに渡す方法は2つです。1つ目は、中身をチャットに貼ること。2つ目は、Projectsの「プロジェクトの指示」に貼るか、ナレッジにファイルとして入れることです。公式ヘルプでは、Projectの指示は「Set project instructions」から保存し、そのProjectのすべてのチャットで使われると説明されています。ナレッジは、プロジェクト画面の右側から「+」で追加します。

## そのまま使えるプロンプト

:::prompt 出典の範囲で書かせる
次のsources.mdに書かれた内容だけを根拠にして、下のテーマについて、300字以内で説明してください。sources.mdに書かれていないことは、書かずに「確認できませんでした」としてください。

【sources.md】
(ここに貼る)

【テーマ】
(ここに書く)
:::

## うまくいかないとき

- **出典に書いていないことを書かれるとき**: 「出典にない内容は、書かない」を、プロンプトの最初に置きます。
- **URLの先が変わっていたとき**: 自分で開いて、確認日と内容を更新します。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
