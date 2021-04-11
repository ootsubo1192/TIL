# 基本コマンド

DBの選択

```mysql
use <schemasname>;
```

DBの表示

```mysql
select * from <tablename>;
```

`*`ですべての列を表示
`<db-name>`の前に`<schemas-name>,`とすることで選択と、表示を一文で実行

コメントアウト、実行しないコマンドの入力

```myseql
-- select * from <tablename>;
```

```mysql
/* use <schemas-name>;
   select * from <tablename>; */
```
 
