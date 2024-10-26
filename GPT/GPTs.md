# ChatGPTGPTsカスタム大全

## ChatGPTをカスタマイズする
- ユーザーアイコンから`ChatGPTをカスタマイズする`を選択
- 指示と回答に対して詳細に設定することで自分に合った回答が生成される

## 日本語フォント
- [IPAex フォント](https://moji.or.jp/ipafont/ipafontdownload/)
- [Noto Sans JP フォント](https://fonts.google.com/noto/specimen/Noto+Sans+JP)

## GPTカスタマイズ
- 機能について
    - コードインタープリターとデータ分析 <br>プログラムをPythonで生成する。データをアップロードして内容を分析することもできる

### Googleカレンダーと連携する
機能はすべて無効

1. GoogleカレンダーAPI利用設定
    1. GCPに登録
    2. APIライブラリから`Google Calendar API`を選択し有効化
    3. 認証情報を作成し、OAuth2.0クライアントIDを作成
        1. 使用するAPIに`Google Calendar API`を選択
        2. アクセスデータの種類に`ユーザーデータ`を選択
    4. OAuth同意画面を入力
    5. スコープを追加で、`Google Calendar API`を有効化
    6. 保存して次へ
2. OAuthクライアントIDの設定
    1. アプリケーションの種類に`ウェブアプリケーション`を選択
    2. 名前に`GPT`を入力
    3. 完了を選択
3. 接続情報の確認
    1. API/サービス詳細から認証情報を選択
    2. 作成したOAuthクライアントIDを選択
    3. クライアントシークレットをコピー
4. テストユーザーの登録
    1. OAuth同意画面で`+ ADD USERS`を選択
    2. ユーザーのメールアドレスを入力して保存
5. GPTの作成
    1. アクションを追加
    2. 認証でOAuthを選択<br>クライアントID： GCPで作成したクライアントID<br>クライアントシークレット: コピーした値<br>認証URL: `https://accounts.google.com/o/oauth2/v2/auth`<br>トークンURL: `https://oauth2.googleapis.com/token`<br>スコープ: `htt@s://www.googleapis.com/auth/calendar.events`
    3. スキーマの記述は、ActionsGPTからヘルプを取得するからプロンプトで生成<br>
    ```txt
    GoogleカレンダーとAPIで連携するGPTを作成したいのですが、OpenAI仕様でカスタムGPT用の正しいスキーマを次を参考に記述してください
    ```
    4. 公開するならプライバシーポリシーのページを作成し、URLを追記
    5. 認証済みのリダイレクトURLが作成されているので、GCPの認証画面で｀承認済みのリダイレクトURI`に追加`

### WebPilotでネット検索の強化
1. GPTを作成する <br>機能: DALL-E 画像生成のみ有効
2. 新しいアクションを作成 <br>認証: なし<br>`https://gpts.webpilot.ai/gpts-openapi.yaml`をURLからインポート<br>プライバシーポリシーに`https://gpts.webpilot.ai/privacy_policy.html`を追加

## GPTストア おすすめ
- StockGPT (Expert stock analyst) <br>株価や市場調査に
- Innovators lens (joel lorange) <br>トレンドや市場動向を調べ、新しいアイデアを提案
- Paper Interpreter (DAICHI KONNO) <br>PDFのファイルURLを指定して要約を作成
- Ai PDF (xuyadong) <br>PDFをアップロードし要約を作成
- GPT FInder (NAIF J ALOTAIBI) <br>GPTのの検索
- Diagrams: Show Me ( Jkmagao) <br>指示やテキストに従いダイアグラムを作成
- Wolfram (wolfram.com) <br>数値に関する問題を扱う
- Grimoire (gptavern.mindgoblinstudios.com) <br>WebサイトやAppの作成支援
- Code Teacher (Karol Munoz) <br>プログラム学習のコーチ
- Go Golang (Widenex) <br>Go言語の質問に答える
- PHP Engineer (Fastlane AI) <br>PHPの質問に答える

