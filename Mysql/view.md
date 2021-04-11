# view コマンドの使い方

### view の作成

```mysql
create view <new-viewname>(<culume>,<culume2>,...)
as 
selct * from <tablename>
    ...;
```

### view の呼び出し

```mysql
select <culme>,<culme>
    from <viewname>
    order by <>;
```

`order by`句はviewに含めることができないのでviewを呼び出してから実行

### view の削除

```mysql
drop <viewname>;
```

