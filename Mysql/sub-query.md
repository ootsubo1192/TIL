# sub query

例：ある商品についてどのユーザーが購入したか調べたい場合

```mysql
select <culems> from <tablename>
    where <id> in (
    select <user_id> from <tablename< ;
```

## scalar sub query

`scalar` -> スカラーという一つの物

例：ある商品の値段の平均値(scalar)よりも<>な値段を表示

```mysql
select * from <tablename> 
    where <price> > (select avg(<price>) from <tablename>)
```

構文の中に構文を作るイメージ

