# git master

## リモートリポジトリの作成

Webの自分のGithubページから作成

Newタブを押下 -> リポジトリ名決める

### Gitの設定ファイル(grobal)

~/.gitconfig

### Gitの設定ファイルの更新

`$ git config --global <attribute> <value>`

--globalをつける -> 当該ユーザーのシステム全体の設定になる(~/.gitconfig)

--globalをつけない -> 実行したリポジトリ独自の設定になる(.git/config)

### Gitユーザーの設定

`$ git config --global user.name "<username>"`

`$ git config --global user.email "<email>"`

設定情報一覧

`$ git config --global --liset`

### リモートリポジトリからcloneしてローカルリポジトリを作成

`$ git clone <remote_repo_url>`

remote_repo_urlはGithubから取得

リポジトリの中に.gitがあればGitのリポジトリとして使用できる。

### ローカルリポジトリに紐付いているリモートリポジトリのURLを確認

`$ git remote -v`

---

Gitは作業履歴をコミット単位で管理します

Gitはファイルの変更を3つのステージに分けて管理する

まず、変更したファイルはWorking-directoryに保存される

---

新規作成ファイルは**untrack**ファイルであり、WorkingareaにはあるがGitは認識しない

一度Staging−areaに追加することでGitで管理することができる

既存のファイルの変更は**track**ファイルでGitの管理下にある

---

次に変更内容をSterging-areaに渡す

最後にリポジトリに渡す

それぞれのコマンドを解説していく

### 作業内容の確認

`$ git status`

working-directory,Staging-areaにどのような変更があるか確認

### 作業内容をStaging-areaに追加

`$ git add <filename>`

特定のファイルをStaging−areaに追加

`$ git add .`

カレントディレクトリは以下のすべての変更ファイル、フォルダをStaging−areaに追加

### Staging-areaの内容をリポジトリにコミット

`$ git commit -m "<commit-message>"`

コミット時には必ずわらりやすいメッセージと書く

コミット後にコミットポイントが作成される

### コミット履歴の確認

`$ git log`

オプションを付けてわかリやすく表示

`$ git log --all --oneline --graph`

--all -> すべての履歴を表示

--oneline -> 縦一列に表示

--graph -> ブランチの流れを線で結ぶ

-- <filename> -> 特定のファイル名の履歴を表示(ファイル名が変更されたら、変更前の履歴は表示されない)

--follow <filename> -> ファイル名の変更も考慮して履歴の表示

### 特定のコミット情報を表示

`$ git show <commitID>`

### リモートリポジトリの更新をローカルリポジトリに反映する

`$ git pull <remote_ref> <branchname>`

指定したリポジトリから指定したプランチの情報を今自分が作業しているブランチに反映

fetchとmergeを同時に処理している

**誰が更新しているかわからないので、必ずpullしてからpushするようにすること**

### ローカルリポジトリの更新をリモートリポジトリに反映

`$ git push <remote_ref> <branchname>`

指定したリポジトリの指定したブランチに、アクティブブランチの情報を送信する

リモートリポジトリの名前は`$ git remote -v`で確認可能

通常は`origin`になっている

### pushしたブランチをmainブランチにマージする

リモートリポジトリはチームで共有するリポジトリなので、自由にマージすることはできない

pull requestsを作成して実行(すべてGithub上で実行していく)

Pull Requestを選択 ->　New Pull Requestを選択(マージするブランチと元になるブランチを選択)

### ローカルリポジトリにリモートリポジトリの内容を反映

ローカルリポジトリでmainブランチに移動

リモートリポジトリのmainブランチの情報をロー各リポジトリのmainブランチにpullする

ローカルリポジトリのmainブランチの内容が更新されたことを確認

**ローカル内だけでマージするのではなく、リモートリポジトリからpullすることでmainブランチを最新にするように**

### unstageする(キャンセル)

- Staging−areaの内容をWorking-areaに戻す

`$ git status`でコマンドを確認できる

`$ git restore --staged <file>`

- Working-areaの内容をunstage

`$ git restore <file>`

変更内容を破棄するのでデータをもとに戻すことはできない

trackファイルのみ変更を受け付ける

### ファイル名の変更をGitで管理する

`$ git mv <filename> <new-filename>`

名前の変更作業が**Staging-area**に追加される

`$ mv <filename> <new-filename>

fileを削除して、同時にUntrackファイルとしてNewfileが作成される

`$ git add -A` -> 削除したファイルとNewfileを同時にStaging−areaに追加、Gitでrenamedファイルとして認識される

### ファイルの削除をGitで管理

`$ git rm <filename>`

untrackファイルは削除できない(Gitの管理下にないので)

Staging-areaのものは削除できない、削除したい時はLinuxのrmコマンドで！

- コミットしたものを削除したが取り消したい場合

削除作業をunstageする -> 削除作業をWorking-areaから削除する(削除したという作業をキャンセルすることでファイルが復活する)

間違ってもリモートリポジトリからpullしてこないように(ローカルリポジトリのほうが進んでいるので、削除したという内容は残ったままになる)

### してしたファイルをGitの管理下から外す

ファイルの作成場所

~/<project>/.gitignore

以下のファイルを追加する

- サイズが大きいファイルやフォルダ(ログファイルや、モデルファイル)

- バイナリーファイル

- 中間ファイル

- パスワードなどの外部に知られては困るファイル

- システムが生成するファイル

書式

example.log -> ファイル名はそのまま記述

*.csv -> すべての.csvファイルを対象に

logs/ -> フォルダは/を使用


