# delete command

### syntax

```mysql
delete * from <table_name>;
```

"delete"で削除したものは基本的にはもとに戻すことができない

大量のデータを"delete"するときには予想外に時間がかかることがある(10万件以上)

## 条件を指定して行の削除

### syntax

```mysql
delete from <table_name> where <column> = <value>;
```

この他にサブクエリを使って条件に合致したものだけを削除することもできる

DB2では動作しない

