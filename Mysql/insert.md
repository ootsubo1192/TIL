# insert command

新規にデータを追加する

### syntax

```mysql
insert into <table_name> (column_name1, column_name2, ...) 
    values('str<values>, int<values>, ...);
```

keyとvalueの数は一致している必要がある

## column を指定せずにデータの追加

## syntax

```mysql
insert <table_name> values(value1, value2, ...);
```

テーブル内のすべての列に対して、値を指定してやる必要がある。
ミスがおこるのであまり使わない。

### 複数行のデータを追加する

## syntax

```mysql
insert into <table_name> (column_name1, column_name2 ...)
    values
    (value1, value2, ...),
    (value1_a, value2_a, ...),
    (value1_b, value2_b, ...);
```

OracleDB　でのこの構文は使用できない

