---
title: Claude CodeとCoworkを徹底比較:使い所・長所と短所・使用例・機能の違い
topic: compare
minutes: 25
features: cowork, claude-code
summary: Claude CodeとCoworkは、どちらも「作業を任せる」ための道具ですが、得意な仕事も、動く場所も、確認の仕組みも違います。公式の情報をもとに、使い所、長所と短所、使用例、機能の差、費用、選び方を、図と表で詳しく整理しました。
added: 2026-11-05
updated: 2026-11-05
next: cowork-vs-claude-code, cowork-scheduled-brief
books:
- はじめての生成AI Claude「超」活用術 | ソーテック社 | 978-4-8007-2163-1
- 今すぐ使えるかんたんEx Claude 仕事術&時短技 | リンクアップ(技術評論社) | 978-4-297-15838-5
- これからのAI×業務改善本格講座 Claude AIで超効率資料作成・情報整理 | 秀和システム新社 | 978-4-7980-7738-3
sources:
- Claude Cowork 製品ページ(Coworkの概要、Claude Codeとの違い、プランと料金、使用量の説明を確認。2026年11月5日に確認) | https://claude.com/product/cowork
- Claude ヘルプセンター「Get started with Claude Cowork」(できること、実行の流れ、許可の3つのモード、対象プラン、制限を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Claude ヘルプセンター「Claude Cowork and chat are one Claude」(チャットとCoworkの統合、展開状況、現在の制限を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude
- Claude ヘルプセンター「Use Claude Cowork on web, desktop, and mobile」(動く場所、各画面で使える機能を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
- Claude ヘルプセンター「Schedule recurring tasks in Claude Cowork」(定期タスクの動き方と頻度を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- Claude ヘルプセンター「Let Claude use your computer in Cowork」(画面操作の対象プラン、許可、安全面を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork
- Claude ヘルプセンター「Organize your tasks with projects in Claude Cowork」(Coworkのプロジェクトの中身を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
- Claude Code ドキュメント「Overview」(Claude Codeの概要、使える場所、できることを確認。2026年11月5日に確認) | https://code.claude.com/docs/en/overview
- Claude Code ドキュメント「Platforms and integrations」(使える場所と連携先の比較を確認。2026年11月5日に確認) | https://code.claude.com/docs/en/platforms
- Claude Code ドキュメント「Extend Claude Code」(CLAUDE.md、スキル、サブエージェント、フック、MCP、プラグインの違いを確認。2026年11月5日に確認) | https://code.claude.com/docs/en/features-overview
- Claude Code ドキュメント「Choose a permission mode」(6つの許可モードと開始時のモードを確認。2026年11月5日に確認) | https://code.claude.com/docs/en/permission-modes
- Claude Code ドキュメント「Get started with Claude Code in the cloud」(クラウドセッションの動き方、対象プランを確認。2026年11月5日に確認) | https://code.claude.com/docs/en/web-quickstart
- Claude Code ドキュメント「Automate work with scheduled tasks」(クラウドの定期タスクと起動の種類を確認。2026年11月5日に確認) | https://code.claude.com/docs/en/routines
- Claude ヘルプセンター「Use Claude Code with your Pro, Max, or Ultra plan」(使用量の共有、上限後の選択肢、APIキーの注意を確認。2026年11月5日に確認) | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
- Claude プランと料金ページ(Pro、Max、Ultraの月額と使用量の違いを確認。2026年11月5日に確認) | https://claude.com/pricing
- Claude ヘルプセンター「Monthly API credits for Max, Ultra, and Team plans」(月ごとのAPIクレジットが、Claude CodeやCoworkに使えないことを確認。2026年11月5日に確認) | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans
- 丸善ジュンク堂書店「はじめての生成AI Claude「超」活用術」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784800721631
- 丸善ジュンク堂書店「Claude AIで超効率資料作成・情報整理」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784798077383
- 丸善ジュンク堂書店「Claude 仕事術&時短技」(書誌情報) | https://www.maruzenjunkudo.co.jp/products/9784297158385
---

## 先に結論

Claude CodeとCoworkは、どちらも「作業そのものを任せる」ための道具です。同じ**エージェント**(自分で計画を立て、道具を使い、結果を見て次へ進むAI)のしくみで動きます。違いは、得意な仕事と、動く場所です。

- **Claude Code**: プログラムやWebサイトなど、**コードそのもの**を直す・作る仕事に向きます。
- **Cowork**: 文書、表、スライド、ファイル整理、調べ物のまとめなど、**コードを使わない仕事**に向きます。
- **チャット**: 質問、相談、文章の下書きなど、1回ずつのやりとりに向きます。

公式の製品ページも、Coworkを「コードを使わない知的作業向け」、Claude Codeを「ソフトウェア開発向け」の道具として説明しています。ただし、境目は絶対ではありません。Coworkも中でコードを動かしますし、Claude Codeも文書を書けます。分かれ目は「**最後に欲しいものが、コードか、資料か**」です。

:::note この解説を読む前に
機能の名前、画面、提供プランは変わることがあります。とくにチャットとCoworkは、いま1つの会話にまとまる途中です。この解説は2026年11月5日時点の公式情報をもとにしています。
:::

## 全体像:3つの入口と、共通のしくみ

:::svg 図: チャット・Cowork・Claude Codeの関係
<svg viewBox="0 0 360 340" role="img" aria-labelledby="g1t g1d" xmlns="http://www.w3.org/2000/svg">
<title id="g1t">チャット、Cowork、Claude Codeの関係図</title>
<desc id="g1d">チャットとCoworkは1つの会話にまとまりつつあります。CoworkとClaude Codeは、同じエージェントのしくみで動きます。コネクタ、スキル、プラグインは、どちらでも使えます。</desc>
<text x="121" y="14" text-anchor="middle" font-size="12" class="t-muted">1つの会話にまとまりつつあります</text>
<path class="ln" d="M8 40 V32 H234 V40"/>
<rect class="b-ch" x="8" y="46" width="108" height="94" rx="10"/>
<text x="62" y="68" text-anchor="middle" font-size="14" class="t-b t-ch">チャット</text>
<text x="62" y="90" text-anchor="middle" font-size="12">質問と相談</text>
<text x="62" y="108" text-anchor="middle" font-size="12">文章の下書き</text>
<text x="62" y="126" text-anchor="middle" font-size="12">1回ずつの会話</text>
<rect class="b-cw" x="126" y="46" width="108" height="94" rx="10"/>
<text x="180" y="68" text-anchor="middle" font-size="14" class="t-b t-cw">Cowork</text>
<text x="180" y="90" text-anchor="middle" font-size="12">資料づくり</text>
<text x="180" y="108" text-anchor="middle" font-size="12">ファイルの整理</text>
<text x="180" y="126" text-anchor="middle" font-size="12">調べ物を丸ごと</text>
<rect class="b-cc" x="244" y="46" width="108" height="94" rx="10"/>
<text x="298" y="68" text-anchor="middle" font-size="14" class="t-b t-cc">Claude Code</text>
<text x="298" y="90" text-anchor="middle" font-size="12">コードを読んで</text>
<text x="298" y="108" text-anchor="middle" font-size="12">直して動かす</text>
<text x="298" y="126" text-anchor="middle" font-size="12">Gitも扱える</text>
<path class="ln" d="M180 140 V160"/><path class="ar" d="M174 156 L186 156 L180 166 Z"/>
<path class="ln" d="M298 140 V160"/><path class="ar" d="M292 156 L304 156 L298 166 Z"/>
<rect class="b-soft" x="8" y="168" width="344" height="62" rx="10"/>
<text x="180" y="192" text-anchor="middle" font-size="14" class="t-b">同じ「エージェント」のしくみ</text>
<text x="180" y="214" text-anchor="middle" font-size="12" class="t-muted">計画する → 道具を使う → 結果を見て次へ</text>
<text x="180" y="256" text-anchor="middle" font-size="12" class="t-b t-muted">どちらでも使える、つなぐ・広げる部品</text>
<rect class="b-base" x="8" y="266" width="108" height="62" rx="10"/>
<text x="62" y="290" text-anchor="middle" font-size="13" class="t-b">コネクタ</text>
<text x="62" y="310" text-anchor="middle" font-size="12">外部とつなぐ</text>
<rect class="b-base" x="126" y="266" width="108" height="62" rx="10"/>
<text x="180" y="290" text-anchor="middle" font-size="13" class="t-b">スキル</text>
<text x="180" y="310" text-anchor="middle" font-size="12">手順を呼び出す</text>
<rect class="b-base" x="244" y="266" width="108" height="62" rx="10"/>
<text x="298" y="290" text-anchor="middle" font-size="13" class="t-b">プラグイン</text>
<text x="298" y="310" text-anchor="middle" font-size="12">まとめて配る</text>
</svg>
:::

公式のヘルプによると、Coworkは「Claude Codeと同じエージェントのしくみを、ターミナルなしで使えるようにしたもの」です。ターミナルは、文字で命令を打つ画面のことです。

チャットとCoworkは、新しい形では1つの会話にまとまっています。先に「チャット」か「Cowork」かを選ぶ必要はなく、Claudeが必要に応じて道具を使います。ただし、展開は段階的です。メッセージ欄に「Chat」と「Cowork」の選択肢が残っていれば、まだ切り替わっていません。一度切り替わると、元には戻せないと書かれています。

Claude Codeは、これとは別の入口を持つ道具です。ただし、コネクタ(MCP)、スキル、プラグインといった部品は、考え方が共通しています。

## それぞれ、何をする道具か

### Cowork:やりたい結果を伝えて、完成品を受け取る

公式のヘルプによると、Coworkは次の順で作業を進めます。

:::flow 図: Coworkが作業を進める流れ
依頼を読んで、計画を立てる | 「やりたい結果」を伝えると、まず進め方を考えます
作業を小分けにする | 複雑な作業は、いくつかの小さな作業に分けます
隔離された環境で実行する | コードやコマンドは、Anthropicのサーバー上の隔離された環境で動きます
並行して進める | 必要に応じて、複数の作業を同時に進めます
完成品を返す | プレビューして、ダウンロードできる形で受け取ります
:::

公式の学習コースは、Coworkに向く仕事を3つの型で説明しています。

- **手順が複数ある仕事**: 情報集め、比較、下書き、整形までを、1回の依頼で任せられます。
- **実際のファイルが中心の仕事**: Word、表、スライド、PDFなどを作ったり、手元のファイルを読んで直したりします。
- **複数のツールにまたがる仕事**: メール、カレンダー、チャットなどをまたいで、情報をまとめます。

### Claude Code:コードの置き場を読んで、直接直す

公式のドキュメントによると、Claude Codeは、コードベース(プログラム一式)を読み、ファイルを編集し、コマンドを実行し、開発ツールとつながる道具です。プロジェクト全体を理解したうえで、複数のファイルにまたがる作業ができます。

:::flow 図: Claude Codeが作業を進める流れ
プロジェクトを開く | ターミナルではフォルダに移動して「claude」と入力します。デスクトップアプリやIDEでも始められます
依頼を書く | 例「このバグの原因を探して、直して」
読む・調べる | ファイルを検索して読み、必要ならWebも調べます
編集・実行する | ファイルを書き換え、コマンドやテストを実行します。確認が必要かどうかは許可モードで決まります
結果を確かめる | 変更の差分(何がどう変わったか)とテストの結果を見て、採用するか決めます
:::

公式の説明では、Claude Codeは「コマンドラインでできることなら何でも」手伝えます。文書を書く、ビルドを動かす、ファイルを探す、調べ物をする、といった作業も含みます。ただし、操作の中心はコードなので、コードを使わない仕事は、Coworkのほうが入口がやさしくなります。

## 動く場所と入口のちがい

:::svg 図: どこで動くか(PCとクラウド)
<svg viewBox="0 0 360 380" role="img" aria-labelledby="g2t g2d" xmlns="http://www.w3.org/2000/svg">
<title id="g2t">Claude CodeとCoworkが動く場所</title>
<desc id="g2d">手元のパソコンでは、Claude Codeがプロジェクトのファイルを直接読み書きします。デスクトップアプリは、Coworkが手元のファイルやブラウザに届くための橋渡しです。クラウドでは、Claude Codeのクラウドセッションと、Coworkのセッションが動き、パソコンを閉じても続きます。</desc>
<rect class="b-soft" x="8" y="8" width="344" height="150" rx="12"/>
<text x="20" y="32" font-size="13" class="t-b">あなたのパソコン</text>
<rect class="b-cc" x="20" y="44" width="150" height="102" rx="10"/>
<text x="95" y="66" text-anchor="middle" font-size="13" class="t-b t-cc">Claude Code</text>
<text x="95" y="86" text-anchor="middle" font-size="12">ターミナル・IDE・</text>
<text x="95" y="102" text-anchor="middle" font-size="12">デスクトップアプリ</text>
<text x="95" y="118" text-anchor="middle" font-size="12">でファイルを直接</text>
<text x="95" y="134" text-anchor="middle" font-size="12">読み書きする</text>
<rect class="b-cw" x="190" y="44" width="150" height="102" rx="10"/>
<text x="265" y="66" text-anchor="middle" font-size="13" class="t-b t-cw">Desktopアプリ</text>
<text x="265" y="86" text-anchor="middle" font-size="12">手元のファイルや</text>
<text x="265" y="102" text-anchor="middle" font-size="12">ブラウザ、画面操作</text>
<text x="265" y="118" text-anchor="middle" font-size="12">への橋渡し役。</text>
<text x="265" y="134" text-anchor="middle" font-size="12">開いている間だけ</text>
<path class="ln-dash" d="M265 150 V244"/>
<path class="ar" d="M259 156 L271 156 L265 146 Z"/>
<path class="ar" d="M259 240 L271 240 L265 250 Z"/>
<text x="257" y="188" text-anchor="end" font-size="12" class="t-muted">フォルダを接続した間だけ</text>
<text x="257" y="206" text-anchor="end" font-size="12" class="t-muted">手元の作業が届く</text>
<rect class="b-soft" x="8" y="216" width="344" height="156" rx="12"/>
<text x="20" y="240" font-size="13" class="t-b">Anthropicのクラウド</text>
<rect class="b-cc" x="20" y="252" width="150" height="108" rx="10"/>
<text x="95" y="274" text-anchor="middle" font-size="13" class="t-b t-cc">Claude Code</text>
<text x="95" y="294" text-anchor="middle" font-size="12">クラウドセッション</text>
<text x="95" y="310" text-anchor="middle" font-size="12">GitHubのコードを</text>
<text x="95" y="326" text-anchor="middle" font-size="12">複製して作業し、</text>
<text x="95" y="342" text-anchor="middle" font-size="12">ブランチで返す</text>
<rect class="b-cw" x="190" y="252" width="150" height="108" rx="10"/>
<text x="265" y="274" text-anchor="middle" font-size="13" class="t-b t-cw">Cowork</text>
<text x="265" y="294" text-anchor="middle" font-size="12">資料づくりの作業</text>
<text x="265" y="310" text-anchor="middle" font-size="12">PCを閉じても続く</text>
<text x="265" y="326" text-anchor="middle" font-size="12">定期タスクも</text>
<text x="265" y="342" text-anchor="middle" font-size="12">ここで動く</text>
</svg>
:::

:::table 表: 入口と動く場所の比較
項目 | Cowork | Claude Code
入口 | Claudeのデスクトップアプリ、Web(claude.ai)、スマホアプリ。Chromeのサイドパネルからも始められる | ターミナル、VS CodeやJetBrainsなどのIDE、デスクトップアプリの「Code」、Web(claude.ai/code)、スマホアプリの「Code」タブ。SlackやCI/CDからも使える
動く場所 | Pro・Max・Ultraでは、新しいセッションはクラウドの隔離環境で動く。TeamとEnterpriseは、管理者の設定で変わることがある | 手元のパソコン(ローカル)か、クラウドの仮想マシン(クラウドセッション)かを選べる
PCを閉じたら | クラウドで動く作業は続く | ローカルは止まる。クラウドセッションは続く。Remote Controlは、PCでセッションを開いている間だけ続く
手元のファイル | デスクトップアプリで接続したフォルダだけ。アプリを開いている間だけ届く | ローカルでは、プロジェクトのフォルダ。クラウドでは、GitHubから複製した範囲
手元の設定 | 指示、メモリ、プロジェクトはアカウントに保存され、どの画面でも共通 | ローカルは、自分の設定とCLAUDE.mdを読む。クラウドは、リポジトリの内容が基本
スマホから | 開始、確認、追加の指示ができる | クラウドセッションの開始と確認、Remote Controlで手元のセッションの操作ができる
:::

用語の補足です。**IDE**は、プログラムを書くための専用ソフトです。**クラウドセッション**は、Anthropicのクラウド上の仮想マシンでClaude Codeを動かす方式です。GitHubにあるコードを複製して作業し、変更を新しい**ブランチ**(作業用の枝分かれ)に保存して返します。**Remote Control**は、手元のPCで動いているClaude Codeを、スマホやブラウザから操作する機能です。

:::note Coworkの「手元のファイル」について
公式のヘルプによると、手元のファイル、ブラウザ、画面操作を使う作業では、Claudeデスクトップアプリを開いたままにしておく必要があります。アプリを閉じると、作業そのものは続きますが、手元のファイルには届かなくなります。
:::

## 得意な仕事と使用例

まず、場面ごとの向き不向きを表にします。これは、公式の説明をもとにした、ここでの整理です。

:::table 表: 場面別の使い分けの目安
場面 | 向く道具 | 理由
会議メモから、報告書やスライドを作る | Cowork | 資料を返してもらう仕事で、コードは関係しない
レシートの写真から、経費の表を作る | Cowork | フォルダのファイルを読んで、表にまとめる仕事
複数のWebページと自分のメモから、比較レポートを作る | Cowork | 調べて、まとめて、ファイルにする一連の仕事
ダウンロードフォルダを、種類と日付で整理する | Cowork | ファイル整理は、公式の例にもある
自分のWebサイトや、アプリのコードを直す | Claude Code | コードを読み、直接書き換える仕事
エラーの原因を探して、直して、テストまで動かす | Claude Code | コマンドを実行して、確かめながら進める仕事
初めて見るコードの全体像を知る | Claude Code | プロジェクト全体を読んで説明できる
変更をGitで記録し、プルリクエストを作る | Claude Code | Gitの操作は、公式の例にもある
ちょっとした質問や、文章の相談 | チャット | 道具を切り替えなくても、会話で済む
:::

つぎに、使用例です。頼み方は、公式の例を参考にここで作った一例です。

:::table 表: Coworkの使用例
場面 | 頼み方の例 | 返ってくるもの
経費の集計 | 「経費フォルダのレシート画像から、日付・店名・金額を表にして。読めない文字は『要確認』と書いて」 | Excelの表と、要確認の件数
会議の整理 | 「添付の議事録から、決定事項と担当者つきの宿題を表にして。A4で1枚のメモにも」 | 表と、1枚のメモ
調査のまとめ | 「小規模チーム向けのプロジェクト管理ツールを3つ調べて、料金と特徴を比較表に。出典のURLつきで」 | 比較表つきのレポート
ファイル整理 | 「ダウンロードフォルダを、種類別・月別のフォルダに整理して。削除はしないで」 | 整理されたフォルダと、移動の一覧
定期のレポート | 「毎週月曜の朝に、先週の予定を振り返って、今週の準備メモを作って」(/scheduleで登録) | 毎週届くメモ
:::

:::table 表: Claude Codeの使用例
場面 | 頼み方の例 | 返ってくるもの
バグの修正 | 「このエラーの原因を探して直して。直したあと、テストを動かして結果を教えて」 | 修正されたファイルと、テスト結果
機能の追加 | 「既存のコードの書き方に合わせて、検索ボックスを追加して」 | 複数のファイルの変更
初見のコードの理解 | 「ファイルは変更しないで。このプロジェクトの構造を、フォルダごとの役割の表で説明して」(Planモード) | 構造の説明
サイトの更新 | 「トップページの説明文を、読みやすく直して。変更前後の差分も見せて」 | 書き換えられたページと差分
スマホからの依頼 | 外出先で、GitHubのリポジトリを選んで「このバグを直して」と送る(クラウドセッション) | 作業用ブランチと、確認用の変更
自動チェック | 「プルリクエストが作られたら、自動でレビューして」(GitHub Actions) | プルリクエストへのレビューコメント
:::

## 長所と短所

:::table 表: 強み
観点 | Cowork | Claude Code
始めやすさ | ターミナルが要らない。普通の言葉で頼める | 入口が多い(ターミナル、IDE、デスクトップ、Web、スマホ)。自分に合う場所を選べる
成果物 | 編集できる文書、Excelの表、スライドなどを返す。公式は、数式つきのスプレッドシートも例に挙げている | コードの変更、テストの実行、Gitのコミット・ブランチ・プルリクエストまで進められる
手放しやすさ | PCを閉じても続く。定期タスクはクラウドで動く | クラウドセッションやクラウドの定期タスクは、PCを閉じても続く
広げやすさ | コネクタ、スキル、プラグイン、プロジェクト、チャットと共有のメモリ | CLAUDE.md、スキル、サブエージェント、フック、MCP、プラグイン、Agent SDK
安全の仕組み | 完全に消す前は、必ず許可を求める。Autoでは自動点検が入る | 6つの許可モード、許可・拒否のルール、Bashのサンドボックス、フック
:::

:::table 表: 弱みと気をつける点
観点 | Cowork | Claude Code
使える条件 | 有料プランのみ。無料プランは対象外 | ターミナル版は、文字で操作する慣れが要る(ここでの整理)。クラウドセッションはGitHubが前提
使用量 | 複数の手順がある仕事は、短い質問より多く使う | Claudeと同じ枠を共有する。長い作業ほど使用量が増える
できないこと | セッションの共有はできない(作った成果物は共有できる)。GitHubからの追加は未対応。旧形式のライブArtifactなどは、デスクトップだけで動く | クラウドは手元の設定が使えない。GitHub以外のリポジトリは制限がある
リスク | 公式は、プロンプトインジェクション(悪意ある指示を紛れ込ませる攻撃)の危険が「ゼロではない」と書いている。画面操作は、間にサンドボックスがない | ファイルが直接書き換わる。確認を飛ばすモードは、隔離された環境だけで使う
:::

## 機能のちがいを一覧で

:::table 表: 仕事と成果物
項目 | Cowork | Claude Code
向く仕事 | 調査、分析、文書づくり、ファイル整理などの知的作業 | ソフトウェアの開発。バグ修正、機能追加、テスト、リファクタリング(中身の整理)
成果物 | ファイル(文書、表、スライド、PDFなど) | コードの変更、テスト結果、Gitの履歴
画面操作 | ベータ。Pro・Max・Ultraで、デスクトップアプリ(macOS・Windows)から | ベータ。Pro・Max・Ultraで、デスクトップアプリとCLI(macOS)から
ブラウザ | Claude in Chromeや内蔵ブラウザで操作できる | Claude in Chromeと連携して、Webアプリの確認や入力ができる
:::

:::table 表: 自動化と広げ方
項目 | Cowork | Claude Code
定期実行 | /scheduleで登録。毎時・毎日・平日・毎週・手動から選ぶ。クラウドで動き、PCがオフでも動く | クラウドの定期タスク(時刻のほか、GitHubのイベントやAPI呼び出しをきっかけにも起動)。デスクトップ版は手元で動く。/loopは開いたセッション内でくり返す
外部アプリとの接続 | コネクタ(Slack、Googleドライブ、カレンダーなど) | MCPサーバー(Googleドライブ、Jira、Slackなど)
手順の再利用 | スキル、プラグイン | CLAUDE.md(毎回読む決まり)、スキル、サブエージェント、フック、プラグイン
並行して動かす | 複雑な仕事では、複数のサブエージェントが並行して動く | サブエージェントのほか、複数のセッションやクラウドの並列タスク
開発ツールとの連携 | Claude for ExcelやPowerPointで、作った表やスライドをさらに編集できる | GitHub Actions、GitLab CI/CD、コードレビュー、Slackの@Claude、Chrome
:::

:::table 表: 記憶・共有・プロジェクト
項目 | Cowork | Claude Code
覚えておく場所 | グローバル指示、プロジェクトの指示、チャットと共有のメモリ | CLAUDE.mdと、Claudeが自動で貯めるメモ
共有 | セッションは共有できない。プロジェクトは、組織の人に「閲覧」「編集」の権限で共有できる | クラウドセッションは共有できる。ProとMaxは「非公開」か「公開」、TeamとEnterpriseは「非公開」か「チーム」から選ぶ
プロジェクト | 指示、定期タスク、コンテキスト、メモリを1つにまとめた作業場 | 別の仕組み。1つの会話から、並行する作業(クラウドセッション)を束ねて管理する
:::

:::note 「プロジェクト」という名前に注意
CoworkのプロジェクトとClaude Codeのプロジェクトは、名前が同じでも別の仕組みです。前者は「資料と指示を置く作業場」、後者は「並行する作業を束ねる会話」です。
:::

用語の補足です。**サブエージェント**は、親のClaudeから仕事を分けてもらい、別の作業場で進める小さなClaudeです。**フック**は、決まったタイミングで必ず動く自動処理です。**MCP**は、外部のアプリとClaudeをつなぐ共通の規格です。**CLAUDE.md**は、作業の約束を書いておき、毎回読ませるファイルです。

## 許可と安全

任せる前に「どこまで勝手に進めてよいか」を決める仕組みが、どちらにもあります。下の図は、確認の強さを並べたものです。

:::svg 図: 確認の強さ(上ほど確認が多い)
<svg viewBox="0 0 360 394" role="img" aria-labelledby="g4t g4d" xmlns="http://www.w3.org/2000/svg">
<title id="g4t">CoworkとClaude Codeの確認の強さ</title>
<desc id="g4d">上から、毎回たずねる、編集は任せる、まず計画だけ見る、自動で点検しながら進む、確認を飛ばす、の順に確認が減ります。Coworkは、Manual、Auto、Skip all approvalsの3つ。Claude Codeは、default、acceptEdits、plan、auto、bypassPermissionsなどのモードがあります。</desc>
<text x="93" y="20" text-anchor="middle" font-size="14" class="t-b t-cw">Cowork</text>
<text x="267" y="20" text-anchor="middle" font-size="14" class="t-b t-cc">Claude Code</text>
<rect x="4" y="30" width="352" height="66" rx="10" fill="#e8eedb"/>
<text x="180" y="50" text-anchor="middle" font-size="12" class="t-b t-muted">毎回たずねる</text>
<rect class="b-cw" x="14" y="56" width="158" height="34" rx="8"/>
<text x="93" y="78" text-anchor="middle" font-size="12">Manual(手動で承認)</text>
<rect class="b-cc" x="188" y="56" width="158" height="34" rx="8"/>
<text x="267" y="78" text-anchor="middle" font-size="12">Manual(default)</text>
<rect x="4" y="102" width="352" height="66" rx="10" fill="#eff2e4"/>
<text x="180" y="122" text-anchor="middle" font-size="12" class="t-b t-muted">編集は任せる</text>
<rect class="b-soft" x="14" y="128" width="158" height="34" rx="8"/>
<text x="93" y="150" text-anchor="middle" font-size="12" class="t-muted">(該当なし)</text>
<rect class="b-cc" x="188" y="128" width="158" height="34" rx="8"/>
<text x="267" y="150" text-anchor="middle" font-size="12">acceptEdits</text>
<rect x="4" y="174" width="352" height="66" rx="10" fill="#f5f3ec"/>
<text x="180" y="194" text-anchor="middle" font-size="12" class="t-b t-muted">まず計画だけ見る</text>
<rect class="b-soft" x="14" y="200" width="158" height="34" rx="8"/>
<text x="93" y="222" text-anchor="middle" font-size="12" class="t-muted">(該当なし)</text>
<rect class="b-cc" x="188" y="200" width="158" height="34" rx="8"/>
<text x="267" y="222" text-anchor="middle" font-size="12">Plan</text>
<rect x="4" y="246" width="352" height="66" rx="10" fill="#fbf1e4"/>
<text x="180" y="266" text-anchor="middle" font-size="12" class="t-b t-muted">自動で点検しながら進む</text>
<rect class="b-cw" x="14" y="272" width="158" height="34" rx="8"/>
<text x="93" y="294" text-anchor="middle" font-size="12">Auto</text>
<rect class="b-cc" x="188" y="272" width="158" height="34" rx="8"/>
<text x="267" y="294" text-anchor="middle" font-size="12">Auto</text>
<rect x="4" y="318" width="352" height="66" rx="10" fill="#f6dcc8"/>
<text x="180" y="338" text-anchor="middle" font-size="12" class="t-b t-muted">確認を飛ばす(信頼できる場合や隔離環境だけ)</text>
<rect class="b-cw" x="14" y="344" width="158" height="34" rx="8"/>
<text x="93" y="366" text-anchor="middle" font-size="12">Skip all approvals</text>
<rect class="b-cc" x="188" y="344" width="158" height="34" rx="8"/>
<text x="267" y="366" text-anchor="middle" font-size="12">bypassPermissions</text>
</svg>
:::

:::table 表: 許可の仕組みの比較
項目 | Cowork | Claude Code
モード | Manual(毎回確認)、Auto(自動で点検)、Skip all approvals(確認なし)の3つ | default(Manualと表示)、acceptEdits、plan、auto、dontAsk、bypassPermissionsの6つ
最初のモード | Pro・Max・Ultra・TeamはAuto、EnterpriseはManualが標準 | 公式の説明では、ターミナルとVS Codeで、v2.1.283以降はautoから始まる。組織の設定などで変わる
Autoの中身 | 各操作を点検し(データの持ち出しやプロンプトインジェクションなど)、危ないものはブロックする。ブロックが続くと、毎回確認に戻る | 別のモデルが、シェルコマンドやネットワーク通信などを点検してから実行する
消す操作 | ファイルを完全に消す前は、必ず明示的な許可を求める | 危険な削除は、モードによって確認が出る。bypassPermissionsでは、ターミナルで時間制限つきの確認が出る
確認を飛ばす | Skip all approvals。公式は、すべてを完全に信頼できるときだけと書いている | bypassPermissions。公式は、コンテナなど隔離された環境だけで使うと書いている。クラウドセッションでは使えない
:::

安全のために、次の点を覚えておくと安心です。

- **「確認なし」は、最初から選ばない**: 慣れるまでは、毎回確認するモードから始めます。
- **大事なファイルはコピーを渡す**: Coworkには、元のファイルではなく、コピーしたフォルダを接続します。Claude Codeでは、Gitで変更前の状態を残しておきます。
- **Autoは万能ではない**: Coworkの公式のヘルプにも、自動の点検はあっても、完全な防御はないと書かれています。お金、他の人へのメッセージ、大事なファイルに関わる作業は、画面の近くで見ているのが安全です。
- **ルールは、モードより強いことがある**: Claude Codeでは、「拒否」のルールは、確認を飛ばすモードでも有効だと書かれています。触らせたくないファイルは、ルールで守れます。
- **画面操作は、特に慎重に**: Coworkの画面操作は、アプリごとに許可を求めますが、間にサンドボックス(外から隔離した安全な箱)がありません。投資や暗号資産のアプリは、標準でブロックされます。健康、お金、個人の記録を扱うアプリでは、使わないことが勧められています。

## 費用と使用量

どちらも、定額プランの「使用量」の中で動きます。下の表は、公式の料金ページをもとにしています。金額は変わることがあるので、申し込む前に料金ページで確かめてください。

:::table 表: 個人向けプランの目安
項目 | Pro | Max | Ultra
月額 | $17(年払いの場合。月払いは$20) | $100 | $200
使用量 | 基準 | Proの5倍(5時間ごと・週ごと) | 週あたりProの10倍。確認済みのアカウントは5時間の上限がない
CoworkとClaude Code | どちらも含まれる | どちらも含まれる | どちらも含まれる
月ごとのAPIクレジット | なし | $100分 | $200分
:::

使用量について、公式から確認できたことをまとめます。

- **ClaudeとClaude Codeは、同じ枠を使います**。5時間ごとの上限と、週ごとの上限があり、どちらの作業も同じ枠から引かれます。
- **Coworkは、チャットより多く使います**。複数の手順を踏む仕事は、コードの実行、ファイルの作成、アプリの利用のたびに使用量が増えます。
- **上限に当たったとき**は、待つ、追加の使用量(usage credits)を使う、Claude Codeの場合はConsoleのAPIクレジットに切り替える、のどれかです。追加の使用量は、標準のAPI料金で課金されます。
- **月ごとのAPIクレジットは、Claude CodeやCoworkには使えません**。自分のアプリやエージェントを作るための別の枠だと書かれています。
- **APIキーに注意**: パソコンに`ANTHROPIC_API_KEY`という環境変数が設定されていると、Claude Codeは、プランの枠ではなくAPI料金で動きます。意図せず課金されないよう、公式のヘルプも注意を促しています。
- **確認の仕方**: 設定の「Usage」で、現在の使用量を見られます。Claude Codeでは、`/usage`でも内訳を確認できます。

## どちらを選ぶか

:::svg 図: どちらに頼むかの判断
<svg viewBox="0 0 360 392" role="img" aria-labelledby="g3t g3d" xmlns="http://www.w3.org/2000/svg">
<title id="g3t">どの道具に頼むかの判断図</title>
<desc id="g3d">最後に欲しいものがコードの変更ならClaude Code、文書や表やスライドの作成やファイル整理ならCowork、質問への答えや文章の相談ならチャットです。どちらでもできそうなときは、最後に欲しいものと、手元のファイルが要るかどうかで選びます。</desc>
<rect class="b-base" x="60" y="8" width="240" height="40" rx="10"/>
<text x="180" y="33" text-anchor="middle" font-size="14" class="t-b">最後に欲しいものは何ですか?</text>
<path class="ln" d="M180 48 V58 H12 V237"/>
<path class="ln" d="M12 97 H26"/><path class="ar" d="M22 91 L22 103 L32 97 Z"/>
<path class="ln" d="M12 167 H26"/><path class="ar" d="M22 161 L22 173 L32 167 Z"/>
<path class="ln" d="M12 237 H26"/><path class="ar" d="M22 231 L22 243 L32 237 Z"/>
<rect class="b-base" x="34" y="70" width="170" height="54" rx="10"/>
<text x="44" y="93" font-size="12">プログラムやWebサイトを</text>
<text x="44" y="111" font-size="12">直す・作る・調べる</text>
<path class="ln" d="M204 97 H230"/><path class="ar" d="M228 91 L228 103 L238 97 Z"/>
<rect class="b-cc" x="240" y="70" width="112" height="54" rx="10"/>
<text x="296" y="93" text-anchor="middle" font-size="13" class="t-b t-cc">Claude Code</text>
<text x="296" y="111" text-anchor="middle" font-size="12">コードの仕事</text>
<rect class="b-base" x="34" y="140" width="170" height="54" rx="10"/>
<text x="44" y="163" font-size="12">文書・表・スライドを作る</text>
<text x="44" y="181" font-size="12">ファイルや情報を整理する</text>
<path class="ln" d="M204 167 H230"/><path class="ar" d="M228 161 L228 173 L238 167 Z"/>
<rect class="b-cw" x="240" y="140" width="112" height="54" rx="10"/>
<text x="296" y="163" text-anchor="middle" font-size="13" class="t-b t-cw">Cowork</text>
<text x="296" y="181" text-anchor="middle" font-size="12">資料の仕事</text>
<rect class="b-base" x="34" y="210" width="170" height="54" rx="10"/>
<text x="44" y="233" font-size="12">質問に答えてほしい</text>
<text x="44" y="251" font-size="12">文章を相談したい</text>
<path class="ln" d="M204 237 H230"/><path class="ar" d="M228 231 L228 243 L238 237 Z"/>
<rect class="b-ch" x="240" y="210" width="112" height="54" rx="10"/>
<text x="296" y="233" text-anchor="middle" font-size="13" class="t-b t-ch">チャット</text>
<text x="296" y="251" text-anchor="middle" font-size="12">会話の仕事</text>
<rect class="b-warn" x="8" y="288" width="344" height="96" rx="10"/>
<text x="20" y="310" font-size="13" class="t-b">どちらでもできそうなとき</text>
<text x="20" y="331" font-size="12">・最後に欲しいものが「コード」か「資料」かで選ぶ</text>
<text x="20" y="350" font-size="12">・両方ある仕事は、2つに分けて別々に頼む</text>
<text x="20" y="369" font-size="12">・手元のファイルが要るか、クラウドで足りるかも見る</text>
</svg>
:::

### 組み合わせて使う例

1つの仕事の中で、道具を使い分けることもできます。たとえば、自分のWebサイトを作って育てる場合です。

:::flow 図: 3つを使い分ける例
チャットで相談する | 作りたいものと、見せたい相手を整理して、必要な機能を決めます
Claude Codeで作る | ページのコードを作り、表示の崩れを直し、変更を記録します
Coworkで資料にする | 紹介用の文書やスライドを作ります
Coworkの定期タスクで見守る | 毎週、アクセスの数字をまとめた報告書を作らせます
:::

## よくある疑問と勘違い

:::table 表: よくある疑問
疑問 | 答え
Coworkは、Claude Codeの置き換えですか | いいえ。公式の製品ページは、Claude Codeはソフトウェア開発向け、Coworkはコードを使わない知的作業向けと、別の道具として説明しています
Coworkはコードを書けませんか | 中でコードを動かして、表やグラフを作ります。ただし、アプリやサイトの開発が目的なら、Claude Codeのほうが向きます
Claude Codeは、エンジニア専用ですか | 公式は「コマンドラインでできることなら何でも」と説明しています。ただし、文字で操作する慣れが要るため、コードを使わない仕事は、Coworkのほうが始めやすいです
Coworkは、なくなるのですか | チャットと1つの会話にまとまり、Coworkでできることが、どの会話からでも使えるようになっています。機能はなくなるのではなく、入口がまとまる形です
無料プランで使えますか | Coworkは有料プランのみと書かれています。Claude Codeは、料金ページに有料プランに含まれると書かれていて、無料プランについての記載は確認できませんでした
スマホだけで使えますか | Coworkは、スマホアプリから開始、確認、追加の指示ができます。Claude Codeは、スマホアプリの「Code」タブから、クラウドセッションやRemote Controlを操作します。スマホは操作の窓口で、コードが動く場所ではありません
Dispatchは使えますか | スマホからデスクトップの作業を頼む機能です。限定ベータで、新しい利用者には提供されていないと書かれています
:::

## 最初の一歩:自分の仕事を振り分ける

いきなり任せるより、まず「自分の仕事が、どの道具に向くか」を整理するのが近道です。次のプロンプトで、1週間分の仕事を振り分けられます。

:::prompt 自分の仕事を3つの道具に振り分ける
次の仕事を、「チャット」「Cowork」「Claude Code」のどれに頼むのが向いているか、表で振り分けてください。
- 今週の仕事: (例: 経費の集計、会議の議事録、自分のWebページの文章直し、取引先へのお礼メール)
- 私の環境: (例: ターミナルは使ったことがない。パソコンはWindows)
表の列: 仕事 / 向く道具 / 理由(1文) / 頼む前に決めておくこと(確認の強さ、渡すファイルの範囲)
確実でないことは「要確認」と書き、推測で断定しないでください。
:::

振り分けができたら、まず1つだけ、消えても困らないコピーのファイルで試してみてください。手順のくわしい版は、下の「つぎに試すなら」にある活用方法で確認できます。
