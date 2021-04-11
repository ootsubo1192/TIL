# select command

```mysql
seletct * from <tablename>;
```

`*`すべての列の表示

```mysql
select <f><culme1>, <culme2> <rename> from <tablename> 
    where <culume> <date> = '20xx-xx-xx;
```

`culme`名の次に`rename`に実際に表示したい名前を表示
`where`文の次に検索したい`culume`の後に方法を指定、演算処理も可能

```mysql
where <culme> >= 20xx-xx-xx and <culme> < 20xx-xx-xx;


`f`には演算処理を書く　例: `avg`, `min`, `max` count(distinct)
`distinct`(明確化):ユニークユーザー数を求める

