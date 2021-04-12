# outer join

片方のテーブルのデータをすべて出力する

外部結合は`null`のデータも含めて取り扱う結合


`inner join`は結合するデータに一致したものだけを出力する

`outer join`は結合するデータに一致していなくても出力する

主キーは出力され、外部キーは値がない`null`になる

syntax

```mysql
select
    <table-name-a>.<column-name>,
    <table-name-b>.<column-name>
from 
    <table-name-a>
left outer join
    <table-name-b>
on <table-name-a>.<coulumn-name> = <table-name-b>.<column-name>;
```

