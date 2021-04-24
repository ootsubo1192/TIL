# update command

### updateの制限の解除(実務では注意する)

```mysql
set sql_safe_updates =0;
```

### syntax

```mysql
update <table_name>
    set <column_name> = <value>, ...;
```

実務ではすべてのデータを更新するということはあまりしないので注意する

## 特定の条件に合致するデータの更新

### syntax

```mysql
update <table_name> set <column_name> = <new_value> 
    where <column_name> = <value>;
```

`where`文を書き忘れるとすべての値が書き換わってしまうので本当に注意する

複数の値を一度に更新することも可能

"set"の後に"<column_name> = <new_value>"を","で続けて書いていく


