# group by

syntax

```mysql
select
    <column-names>
from
    <table-name>
group by
    <column-names>;
```

`group by`で指定した列名をグループ分けする
グループ分けして列に対する集計方法を`select`文に書く

例

```
select
    count<column-name-a>
from
    <table-name>
group by
    <column-name-a>
```

