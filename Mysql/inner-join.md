# inner join

syntax

```mysql
select
    <table-name-a>.<column-name>,
    <table-name-b>.<column-name>
from
    <table-name-a>
inner join
    <tabele-name-b>
on <table-name-a>.<column-name> = <table-name-b>.<column-name>;
```

はじめに結合したいテーブル名を指定、次に`from`で指定したテーブルの列名に
結合したいテーブルの列名を指定する。

`select`に結合したテーブルの列名を指定可能

