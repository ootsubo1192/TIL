# PKCE

Proof Key for Code Exchange の略

## 何をやるのか

検証コードと乱数を使用してチャレンジコードを作成する。

認証要求の際ににチャレンジコードと乱数に使用した方法として`code_challenge_method`をパラメータとして送信する。

次に、アクセストークンの要求時に、検証コードを送る。

その後、検証コードを`code_challenge_method`でハッシュ化したものとチャレンジコードが一致することを検証する。

OAuth2.0の拡張機能。

`code_challenge_method`がS256であれば、検証コードをSHA-256でハッシュ化しbase64urlエンコードした値がチャレンジコードになる。
