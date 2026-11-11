---
title: Claude SheetsとClaude Whiteboardsがベータで登場。有料プランで使えます
date: 2026-11-10
summary: 2026年11月10日に、Claudeで表を作るClaude Sheetsと、みんなで発想を出し合うClaude Whiteboardsが、ベータで始まりました。有料プランが対象で、Excelの全機能には対応していません。Claude Meetingsは「近日公開」と案内されています。
features: artifacts, docs-slides
added: 2026-11-12
updated: 2026-11-12
next: slides-from-notes
sources:
- Claude「Introducing Claude Whiteboards, Claude Sheets, and Claude Data」(2026年11月10日の発表。SheetsとWhiteboardsのベータ開始、機能、対象プラン、管理者の設定、Sheetsの制限。2026年11月12日に確認) | https://claude.com/resources/articles/sheets-whiteboards-data
- Claude「More ways to work with Claude: Sheets, Whiteboards, and Interactive Connectors」(2026年11月10日の発表。Meetingsが近日公開と案内されていること。2026年11月12日に確認) | https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors
---

2026年11月10日に、Anthropicは、Claude SheetsとClaude Whiteboardsをベータ(試験的な提供)で始めました。要点は3つです。Sheetsは、数式やタブのある表を、Claudeと作る機能です。Whiteboardsは、共有のボードで、Claudeと発想を出し合う機能です。どちらも有料プランが対象で、ベータのため、機能は変わることがあります。

「会議のたびに、付箋の整理と議事メモの清書に時間がかかる」と悩んでいるチームの人に、そのまま見せられる内容です。

## 何が発表されたか

公式の発表(2026年11月10日、2026年11月12日に確認)には、次のように書かれています。

- Claude Sheets(ベータ): タブ、数式、書式、ドロップダウンのある表を、Claudeが作る。「キャンペーン管理表」や「採用予算」のような依頼から作れる。セルを直すときは、変更点が分かり、変更の履歴をたどれる。チームで共有して、一緒に編集できる。
- Claude Whiteboards(ベータ): 共有のボードで、チームがClaudeと発想を出し合う。ふりかえりの会議で、各自が書いたメモを、Claudeがテーマ別にまとめ、各人のやることの下書きを作る、という例が挙がっている。ボードの一部を選んで、その部分についてClaudeに質問できる。終わったあと、ボードを文書やスライドにできる。
- Claude Data(以前の名前はClaude Dashboards): 同じ日に、正式版になった。企業のデータに素早く質問する機能で、この記事では詳しく扱いません。

あわせて、別の発表ページには、Claude Meetingsは「近日公開」と書かれています。通話にClaudeが加わり、議事録を取れる、という説明です。提供の時期や対象プランは、確認できませんでした。

## できるようになること

公式の発表をもとに、3つの機能を並べます。

:::compare 図: 今回の主な機能(公式の発表の整理)
機能 | 内容と状態
Claude Sheets | 数式やタブのある表をClaudeと作る。ベータ
Claude Whiteboards | 共有のボードでClaudeと発想を整理する。ベータ
Claude Meetings | 通話に加わって議事録を取る。近日公開(時期・対象は確認できませんでした)
:::

対象プランと使える場所は、公式の発表に次のように書かれています。

- 対象プラン: すべての有料プランで使える。無料プランについての記載は、確認できませんでした。
- 使える場所: Web、デスクトップ、モバイル。
- 管理者の設定(組織のプランの場合): Teamプランでは、3つの機能は、初めからオン。Enterpriseプランでは、WhiteboardsとSheetsは初めからオフで、「Organization settings > Artifacts」で変更する。Claude Dataは、2026年11月19日に、初めからオンになる。

Sheetsの制限も、公式の発表に書かれています。現時点では、シンプルな表の機能で、機能は今後増える予定です。Excelの全機能が必要なときは、.xlsxやCSVで書き出すか、Claude for Excelを使う、という案内です。

## 活用方法

使うかどうかの目安は、「小さな表や、会議のメモを、早く形にしたいか」です。

試し方を1つ示します。まず、練習用のデータで、個人情報の入らない内容で試します。

:::prompt Sheetsで、小さな予算表を作る
Claude Sheetsで、「学園祭のクラス出店の予算表」を作ってください。
- 列: 項目、単価、個数、小計、メモ。
- 項目の例: 材料費、袋代、ポスター代。数字は、私が後から入れる。仮の数字は入れない。
- 最下段に、小計の合計を出す数式を入れる。
- 個数の列は、0以上の整数だけ入れられるようにする。
作ったあとで、数式の入っているセルを一覧にして、何を計算しているかを1行ずつ書いてください。
:::

作れたら、仮の数字を入れて、合計が自分の電卓と合うかを確かめます。Whiteboardsは、同じ要領で、ふりかえりのメモ(「良かったこと」「困ったこと」)を数件入れて、テーマ別にまとめてもらうと、動きが分かります。

## 注意すること

- どちらもベータです。機能や画面は、変わることがあります。
- Sheetsは、Excelの全機能には対応していません。複雑な計算は、書き出して、別のソフトで確かめます。
- Claudeが作った数式は、自分で検算します。合計が合うかを、電卓や別の表で確かめます。
- 共有するときは、見せてよい範囲かを確かめます。個人情報や、社外に出せないデータは、入れません。
- 無料プランで使えるか、地域による違い、容量の上限は、確認できませんでした。使う前に、公式の案内で確かめます。
- Claude Meetingsは「近日公開」の案内だけで、今は使えるとは限りません。
