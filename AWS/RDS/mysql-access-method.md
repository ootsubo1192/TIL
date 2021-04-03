# mysqlサーバーへの接続方法

まずは[Mysql Cliant](https://login.oracle.com/mysso/signon.jsp)を
Oracleにログインしてインストール

ターミナルから接続できるように <dt>$PATH</dt> 通す必要がある
※後で記載します。

EC2インスタンスを作成しssh接続をし、Mysqlクライアントのインストール

```bash
$ sudo yum localinstall -y https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
```

続いて

```bash
S sudo yum install -y mysql-community-client
```

インストールされたことの確認

```bash
$ mysql --version
```

接続を確認できたら、Mysqlにログイン

```bash
$ mysql -u<username> -p<password> -h<RDSendpoint>
```

