# データ転送 scpの使用方法

ターミナルに接続して、インスタンスに接続せずに実行

```bash
$ scp -i <keyfile> <transfer-data> ec2-user@<publicIP>:<path>
```

オプション
<dt>-i</dt> 	秘密鍵の使用