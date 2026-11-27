---
title: Claudeに頼んで、無料のAIで画像を作り、GitHubのページに貼る
level: intermediate
minutes: 30
purpose: build
features: claude-code
output: 画像を自動で作る仕組み(GitHub Actions)と、実際に作った画像4枚
summary: 画像は別の無料AI(Cloudflare Workers AIのFLUX.1 schnell)に作らせ、仕組みづくりと貼り付けはClaudeに頼む方法です。方法の比較、設定の一覧、手順、実際の失敗と作った画像4枚を、図と表で載せました。
added: 2026-11-28
updated: 2026-11-28
next: cloud-environment-setup
sources:
- Cloudflare Docs「Workers AI Pricing」(1日の無料枠、画像生成モデルの料金。2026年11月28日に確認) | https://developers.cloudflare.com/workers-ai/platform/pricing/
- Cloudflare Docs「flux-1-schnell」(入力項目と出力の形式。2026年11月28日に確認) | https://developers.cloudflare.com/workers-ai/models/flux-1-schnell
- Cloudflare Docs「Workers AI REST API」(APIトークンとアカウントIDの取り方。2026年11月28日に検索結果で確認) | https://developers.cloudflare.com/workers-ai/get-started/rest-api
- Cloudflare Docs「Workers AI Limits」(画像生成の毎分の上限。2026年11月28日に確認) | https://developers.cloudflare.com/workers-ai/platform/limits/
- Cloudflare「Workers AI」(クレジットカードなしで始められる旨。2026年11月28日に検索結果で確認) | https://www.cloudflare.com/product/workers-ai
- GitHub Docs「How use of GitHub Actions is measured」(公開リポジトリの標準ランナーは無料。2026年11月28日に検索結果で確認) | https://docs.github.com/en/billing/concepts/product-billing/github-actions
- GitHub Docs「Using secrets in GitHub Actions」(Secretsの登録の手順と注意。2026年11月28日に検索結果で確認) | https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- GitHub Docs「About the GITHUB_TOKEN」(書き込み権限の指定と、Pagesの公開についての注意。2026年11月28日に検索結果で確認) | https://docs.github.com/en/actions/automating-your-workflow-with-github-actions/authenticating-with-the-github_token
- Claude Code Docs「Configure cloud environments」(クラウドセッションの接続先の制限。2026年11月28日に検索結果で確認) | https://code.claude.com/docs/en/cloud-environments
- Hugging Face「FLUX.1-schnell」(モデルのライセンス。2026年11月28日に検索結果で確認) | https://huggingface.co/black-forest-labs/FLUX.1-schnell
---

画像は別のAIに作らせ、**Claudeは仕組みづくりと貼り付けだけ**を担当します。自分でやるのは、鍵の登録だけです。

## ねらい

- 同じ仕組みを、自分のサイトに作れるようになります。
- 他の方法との違いと、選んだ理由が分かります。
- 実際に起きた失敗を先に知って、止まらずに進められます。

## 準備するもの

:::compare 図: 準備するもの
もの | 条件
GitHubのリポジトリ | **公開**であること(Actionsの無料条件のため)
Cloudflareのアカウント | 無料。カード登録なしで始められる
Claude Codeなど | リポジトリを変更できるClaude
時間 | 30分ほど
:::

## 方法の比較

:::compare 図: 画像をサイトに入れる3つの方法
方法 | 画像を作る場所 | 自分の手間 | 今回
Claudeだけで作る | Claude | 少ない | 写真風・イラスト風の画像ファイルは作れない
Claude Codeから直接、画像AIを呼ぶ | Claudeの作業環境 | 環境の接続先設定と鍵の登録 | 設定すれば可能(公式)。未検証
GitHub Actionsから呼ぶ | GitHubの実行環境 | 鍵の登録 | **採用。実際に動いた**
:::

:::compare 図: 画像AIに選んだサービス
項目 | Cloudflare Workers AI(FLUX.1 schnell)
料金 | 1日10,000ニューロンまで無料。超えるとエラーで止まる
カード登録 | 不要
呼び出し方 | REST API(URLに送るだけ)
モデルのライセンス | Apache 2.0(Hugging Faceのモデルカード)
:::

他のサービスとの細かい料金比較は、この記録には載せていません。

## 全体の流れ

:::flow 図: 全体の流れ
自分: トークンとIDを取る | Cloudflareで2つの値を控える
自分: Secretsに登録する | Claudeには見せない
Claude: 仕組みを作って送る | スクリプト、設定ファイル、説明文の一覧
GitHub Actions: 画像を作る | 一覧が変わると自動で動き、保存する
Claude: 見て確かめて貼る | 問題のある画像は使わない
:::

## 手順

### 1. Cloudflareでトークンを取る

:::flow 図: Cloudflareでの操作
「AI」→「Workers AI」を開く | ダッシュボードの左のメニュー
「Use REST API」を選ぶ | トークンとIDの欄が出る
「Create a Workers AI API Token」を押す | テンプレートのまま作る
「Create API Token」→「Copy API Token」 | 画面を閉じると再表示できない
「Get Account ID」の値をコピー | 2つとも手元に控える
:::

:::compare 図: トークンの設定
項目 | 値
権限 | Workers AI - Read と Workers AI - Edit の両方(テンプレートで入る)
置き場所 | 控えるだけ。チャットには貼らない
:::

### 2. GitHubのSecretsに登録する

:::flow 図: GitHubでの操作
リポジトリの「Settings」を開く | 画面の上のほう
「Secrets and variables」→「Actions」 | 左のメニュー
「New repository secret」を押す | 2回行う
名前と値を入れて「Add secret」 | 名前は下の表のとおり
:::

:::compare 図: 登録する2つ
名前(そのまま入力) | 値
CLOUDFLARE_API_TOKEN | 手順1のAPIトークン
CLOUDFLARE_ACCOUNT_ID | 手順1のアカウントID
:::

名前は英数字とアンダースコアだけです。設定ファイルと1文字違わず合わせます。

### 3. Claudeに仕組みを頼む

リポジトリを開いたClaude Codeに、次を貼ります。

:::prompt 仕組みを作ってもらう
このリポジトリに、画像を自動で作る仕組みを足してください。
- 画像は Cloudflare Workers AI の @cf/black-forest-labs/flux-1-schnell で作る
- 説明文の一覧は data/image-prompts.json。項目は id、prompt、steps
- tools/gen_image.py が、まだない画像だけを作って docs/img/gen/ に保存する。Pythonの標準ライブラリだけで書く
- GitHub Actions の設定は .github/workflows/generate-images.yml。一覧が変わったときと、手動で動く
- 鍵は Secrets の CLOUDFLARE_API_TOKEN と CLOUDFLARE_ACCOUNT_ID から読む。表示もファイルへの書き出しもしない
- 1回で作る枚数に上限を付ける
- 失敗したときは、Cloudflareの返事の本文を表示する
- 作った画像はActionsがそのままコミットする
Secrets は登録済みです。書き終えたらGitHubに送り、Actionsの結果を確認して、失敗したら原因を教えてください。
公式ドキュメントで確認できない入力項目は、使わないでください。
:::

### 4. 説明文の一覧を書く

:::prompt data/image-prompts.json の形
[
  {
    "id": "idea-bubble",
    "prompt": "Minimal flat illustration of a glowing light bulb next to a speech bubble on a pastel blue background, simple shapes, no text",
    "steps": 4
  }
]
:::

:::compare 図: 項目の意味
項目 | 意味 | 値
id | 画像のファイル名になる | 英数字とハイフン
prompt | 作りたい絵の説明 | 2048文字まで。**英語**で書く
steps | 仕上げの回数 | 1〜8、初期値4
seed | 同じ絵を作り直すための値 | **送ると400エラー。使わない**
:::

一覧を保存してGitHubに送ると、Actionsが自動で動きます。

### 5. 画像を見て、貼ってもらう

:::prompt 確かめて貼ってもらう
docs/img/gen/ の画像を1枚ずつ見て、次を教えてください。
- 説明文のとおりの絵か
- 実在するメーカーのロゴ、既存のキャラクター、人の顔に似た絵が入っていないか
- 文字のような模様が入っていないか
問題のない画像だけを、ページの○○の下に貼ってください。代替テキストは、絵の内容が分かる短い文にしてください。
問題のある画像は、作り直す前に、何が問題か教えてください。
:::

## 設定の一覧

:::compare 図: 今回動いた設定
場所 | 項目 | 値
Actionsの設定 | 動くとき | 手動、または data/image-prompts.json が変わったとき
Actionsの設定 | permissions | contents: write(画像をコミットするため)
Actionsの設定 | 実行環境 | ubuntu-latest
スクリプト | 画像の大きさ | 1024×1024px(今回は指定せず、この大きさで出た)
スクリプト | 1回の上限 | 8枚
スクリプト | steps | 4(比較用に1枚だけ8)
Cloudflare | 毎分の上限 | 画像生成は毎分720回まで(公式)
Cloudflare | 無料枠の更新 | 毎日UTC0時(日本時間9時)
:::

:::output .github/workflows/generate-images.yml(実際に使ったもの)
name: 画像を生成する
on:
  workflow_dispatch:
  push:
    paths:
      - data/image-prompts.json
permissions:
  contents: write
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: 画像を生成する
        run: python3 tools/gen_image.py
        env:
          CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
      - name: 生成した画像をコミットする
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add docs/img/gen data/image-results.json
          git diff --cached --quiet || (git commit -m "画像を生成" && git push)
:::

## 実際の出力例

1回目は失敗しました。

:::output 1回目のログ(失敗)
[1/4] desk-steps4: 失敗 HTTP 400 {"errors":[{"message":"AiError: Bad input: Error: Additional or unevaluated properties '/seed' at '/' not allowed …","code":5006}],"success":false}
:::

原因は、公式の例にあった「seed」を送ったことでした。外して再実行すると、成功しました。

:::output 2回目のログ(成功)
[1/4] desk-steps4: 成功 1024x1024px 435KB 1.8秒 steps=4
[2/4] desk-steps8: 成功 1024x1024px 507KB 3.0秒 steps=8
[3/4] desk-ja: 成功 1024x1024px 349KB 2.3秒 steps=4
[4/4] idea-bubble: 成功 1024x1024px 178KB 1.6秒 steps=4
:::

作った画像です。**すべてAI(FLUX.1 schnell)が作りました。** 絵の内容は、私が目で見て書きました。

:::image 実際に作った画像4枚
img/gen/desk-steps4.jpg | 机を上から見た絵。ノートパソコン、ノート、紅茶、観葉植物がある | steps=4。英語の説明文で、ほぼ指定どおり。紅茶が2杯になった
img/gen/desk-steps8.jpg | 机を上から見た絵。ノートパソコンが2台、紅茶、ノート、観葉植物がある | steps=8。同じ説明文で、パソコンが2台になった
img/gen/desk-ja.jpg | 白い背景に、お椀に入った黄色いスープと卵のような丸いもの。文字のような赤と黒の模様がある | 日本語の説明文。机の絵にならず、お椀の絵と文字のような模様になった(1回だけの試行)
img/gen/idea-bubble.jpg | 水色の背景に、黄色い電球と、中が空の白いふきだし | 図形だけの指定は、指定どおりになった
:::

:::compare 図: 使った量(見積もり)
項目 | 値
1024×1024・steps=4 | 1枚 57.6ニューロン
1024×1024・steps=8 | 1枚 96ニューロン
今回の7枚の合計 | 約520ニューロン(無料枠の約5%)
:::

数字は、公式の料金表から私が計算した見積もりです。実際の量は、Cloudflareの画面で確かめられます。

## 使いどころと失敗例

:::compare 図: 向き・不向き
向く | 向かない
ページの飾り、背景の絵 | 日本語の説明文をそのまま使う
単純な図形の絵 | 数や位置を指定どおりにする
同じ作り方で数枚〜数十枚 | 実在のものに似てはいけない場面
:::

:::compare 図: 起きたこと
起きたこと | 直し方
seedを送って400エラー | seedを外す。同じ説明文でも、毎回違う絵になる
日本語の説明文が、お椀の絵になった | 英語にする。英語なら必ず通るかは未確認
実在メーカーのロゴに似た絵が入った(机の絵5枚中2枚) | 公開せず、作り直した。「ロゴなし」と書いても入ることがあった
steps=8の効果が分からない | 同じ絵で比べられないため、判断できない。時間はどちらも数秒
:::

## うまくいかないとき

:::flow 図: 止まったときの確認順
Actionsの結果を見る | リポジトリの「Actions」タブ。赤い×の実行を開く
ログの最後を読む | HTTP 400なら説明文や項目、401/403なら鍵や権限
Secretsの名前を見る | 大文字小文字、アンダースコアまで同じか
無料枠を見る | 超えるとエラーで止まる。翌日(UTC0時)に戻る
手動で再実行する | 「Run workflow」を押す
:::

- ページに反映されないとき: 公式には、ActionsのGITHUB_TOKENによるコミットではPagesの公開が動かない、という注意があります。今回は動きました。動かない場合の直し方は、確認できていません。
- 画像が重いとき: 1枚180〜520KBでした。並べる数が多いなら、小さくしてもらいます。

## 公開前の点検

:::compare 図: 点検リスト
確かめること | 方法
ロゴ、キャラクター、人の顔に似ていない | 画像を目で見る
文字のような模様が入っていない | 画像を目で見る
AI画像だと分かる | ページに書く
商用で使える | Cloudflareの利用条件を自分で読む(今回は未確認)
鍵が表に出ていない | チャットにも、ファイルにも書かない
:::

無料枠の数字や画面は変わることがあります。使う前に、公式ページで確かめてください。
