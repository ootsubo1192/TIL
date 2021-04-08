# 基本コマンド

DBの選択

```mysql
use <schemas-name>;
```

DBの表示

```mysql
select * from <db-name>;
```

`*`ですべての列を表示
`<db-name>`の前に`<schemas-name>,`とすることで選択と、表示を一文で実行

コメントアウト、実行しないコマンドの入力

```myseql
-- select * from <db-name>;
```

```mysql
/* use <schemas-name>;
   select * from <db-name>; */
```
 
