# create table

データベースに新規でテーブルの作成

### syntax

```mysql
create table books(id int not null auto_increment primary key,
    title varchar(255) not null);
```

"()"内はテーブルにどんな情報を入れるか指定している

### id(column_name)

- int -> 整数型

- not null -> nullを許可しない

- auto_increment -> idを自動的に入力

- primary key -> 主キーの設定

#### title(column_name)

- varchar(255) -> 最大255文字の可変長文字列型

- not null -> nullを許可しない

## テーブルの情報の確認

```mysql
show columns from <column_name>;
```

## テーブル構造の変更

```mysl
alter table <table_name> add <new_column_name> int after <columns_name>;
```

- add -> 新しいテーブルの作成

- after -> 指定したテーブル名の後に配置

### 列のの削除

```mysql
alter table <table_name> drop <column_name>;
```
