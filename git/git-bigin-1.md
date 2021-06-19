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


