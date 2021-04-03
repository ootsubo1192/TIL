# EC2で踏み台サーバーを設置、サーバー経由でDB接続

インスタンスからDBに接続できる状態にする。
別のインスタンスを踏み台サーバーとして立ち上げる

```bash
$ ssh -i <keyfile> -NL <rocalport>:<DBendpoint>:<DBport> ec2-user@<pablicIP>
```

問題なく接続されていれば何も表示は出ない
続いて、ローカルのターミナル画面から(Mysqlの場合)

```bash
$ mysql -u<username> -p -h<127.0.0.1> -P<rolacport>
```

接続されればMysqlの画面が立ち上がります
- ローカルポートは何番でもいい
- ホストポートの番号が　<dt>127.0.0.1</dt> なのは理解できていない。わかれば追記