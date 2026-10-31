---
title: MaxとTeamのプランに、毎月のAPIクレジットが付くように(Maxは月100ドル分)
date: 2026-10-07
summary: 2026年10月7日の発表です。MaxやTeamなどのプランに、自作のアプリやエージェントをClaude Platformで動かすための、毎月のAPIクレジットが含まれるようになりました。受け取るには、Console組織をひも付けます。
features:
added: 2026-11-01
updated: 2026-11-01
next: artifact-mini-tool
sources:
- Claude ヘルプセンター「リリースノート」(2026年10月7日の項目「Monthly API credits for Max and Team plans」) | https://support.claude.com/en/articles/12138966-release-notes
- Claude ヘルプセンター「Monthly API credits for Max, Ultra, and Team plans」(金額、対象プラン、受け取り方、対象外の利用の確認。2026年11月1日に確認) | https://support.claude.com/en/articles/17154008
---

## 何が発表されたか

Claudeの公式リリースノート(2026年10月7日)によると、MaxとTeamのプランに、自分のアプリやエージェントをClaude Platformで動かすための「毎月のAPIクレジット」が含まれるようになりました。数日かけて順に始まる、とも書かれています。受け取るには、Claude Consoleの組織をひも付けます。

詳しい条件は、リリースノートからリンクされている公式のヘルプ記事(2026年11月1日に確認)に書かれています。

- **対象プラン**: Max、Ultra、Team(割引のTeamプランを含む)です。Free、Pro、Enterpriseは対象外と書かれています。なお、リリースノートの項目名にUltraは出てきませんが、ヘルプ記事の題名にはUltraが入っています。
- **金額(1か月あたり)**: Maxは100ドル、Ultraは200ドルです。Teamは、Standardの席が1つにつき20ドル、Premiumの席が1つにつき100ドルで、全員分をまとめて使えます(上限は月500ドル)。
- **受け取る条件**: プランが有効であること。新しく登録した場合は、対象プランで7日たってから受け取れます。

## できるようになること

- Claude PlatformのAPI(Messages APIなど)、Console内のPlayground、Claude Managed Agents、Claude Agent SDKを、クレジットの範囲で動かせます。
- クレジットはConsoleの請求ページに、金額と期限つきで表示されます。クレジットは、購入したクレジットより先に使われます。
- 使ってもClaudeのプランの使用量の上限には影響しない、と書かれています。

受け取り方(MaxまたはUltraの場合)は、ヘルプ記事によると次のとおりです。

1. ブラウザでclaude.aiを開き、「Settings」→「Billing」へ進みます(Teamは、OwnerまたはPrimary Ownerが「Organization settings」→「Billing」へ)。
2. 「API credits」の項目で「Link organization」を選びます。
3. ひも付けるConsole組織を選ぶか、新しく作ります。
4. 補足クレジットの規約を読んでから、「Link organization」を押します。

## 活用方法

自作の小さなツールや、自動化のアイデアを、APIで試すときの元手として使えます。ただし、APIには、プログラムを書く手間と、Consoleの設定が必要です。まず「何を作りたいか」を決めるところは、チャットで進められます。

:::prompt 試し方: APIで作れそうなものを、小さく決める
私は、Claude APIを使って、小さなツールを1つ作ってみたいです。プログラミングの経験は(ほとんどない / 少しある / ある)です。
次の順で、私に質問してください(一度に聞くのは2つまで)。
1. 毎週くり返している作業で、文章を読む・書く・分ける作業は何か
2. その作業の「入力」と「出力」は何か
3. 失敗したとき、困るのはどの程度か
答えが出そろったら、最初の1週間で試せる、いちばん小さな案を1つだけ出してください。費用の見積もりは、公式の料金ページで確かめるべき点として挙げ、あなたの推測で金額を書かないでください。
:::

## 注意すること

- 対象は、Max、Ultra、Teamです。ProやFreeでは受け取れません。
- 受け取りはclaude.aiのブラウザ画面で行います。ひも付ける組織は1つだけで、あとから自分では変更できない、と書かれています(変更はサポートへの連絡が必要)。
- 対象外の利用があります。ヘルプ記事によると、対話型のClaude Code(ターミナル、IDE、デスクトップ、Web)、Claude・Claude Code・Coworkの追加利用、Bedrock・Vertex AI・Microsoft Foundry経由のClaudeには使えません。
- クレジットは請求期間ごとに更新され、繰り越されません。使い切ったときは、購入したクレジットや自動チャージがなければ、次の付与までAPIの要求が止まります。
- 金額や条件は変わることがあります。受け取る前に、公式のヘルプ記事で最新の内容を確かめてください。
- 日本での提供について、リリースノートやヘルプ記事の取得できた範囲では、地域の制限は確認できませんでした。
