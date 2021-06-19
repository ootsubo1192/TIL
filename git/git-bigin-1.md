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

--graph -> ブランチの流れをわかりやすく図を使って表示

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

Staging−areaの内容をWorking-areaに戻す


