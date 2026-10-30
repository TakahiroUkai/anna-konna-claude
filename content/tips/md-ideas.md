---
title: ideas.mdに、案をためて、Claudeと選び分ける
level: beginner
minutes: 10
purpose: organize
features: chat
output: 案を置いておくメモ(ideas.md)
summary: 思いついた案を、ideas.mdにいったんためておき、Claudeと「やる・待つ・やめる」に分ける方法です。
added: 2026-10-30
updated: 2026-10-30
next: md-todo
sources:
- Claude ヘルプセンター「Upload files to Claude」(対応するファイル形式、チャットの上限。2026年10月30日に確認) | https://support.claude.com/en/articles/8241126-uploading-files-to-claude
- Claude ヘルプセンター「How can I create and manage projects?」(Projectの指示とナレッジの設定。2026年10月30日に確認) | https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
---

案は、思いついた瞬間には光って見えても、時間がたつと色あせます。ideas.mdは、案をいったん置いておく場所です。todo.mdと分けておくと、やることが散らかりません。

## ねらい

- 思いつきを逃さず、やることとは分けて置きます。
- 時間をおいて、冷静に選び直せます。
- 案ごとに「確かめること」を添えます。

## 準備するもの

- 案を5〜10個。1行で十分です。
- 案ごとの「何が分かれば始められるか」。

## 手順

:::flow 図: ideas.mdを作って、選び分けるまで
1行で書き足す | 思いついたらすぐに
週に1度まとめて見る | 数が増えたときが目安
Claudeと仕分ける | 下のプロンプトで、やる・待つ・やめるに分ける
やるものを todo.md へ移す | 次の1歩まで具体的にして移す
:::

画面の表示は変わることがあります。見つからないときは、公式ヘルプを確認してください。

## そのまま使えるプロンプト

:::prompt 案を仕分ける
次のideas.mdの案を、「すぐやる」「確かめてからやる」「やめる」に分けてください。分けた理由を1文ずつ書き、「確かめてからやる」には、何を確かめればよいかも書いてください。収益や成果が出るとは、書かないでください。

(ここにideas.mdを貼る)
:::

## うまくいかないとき

- **案が全部よく見えるとき**: 「1週間で試せるものだけ」と条件を足します。
- **案が増えすぎたとき**: 「やめる」にした案は、削除せず、理由つきで別の場所に残します。
- ファイルとして渡すときの注意: 公式ヘルプの対応形式の一覧(PDF、DOCX、CSV、TXT、HTML、ODT、RTF、EPUB、JSON、XLSX)に、.mdは載っていません。通るか不安なときは、中身を貼るか、拡張子を.txtにして渡します。
