# リポジトリ

## スクラッチからリポジトリの作成

`$ git init <project-name>`

カレントディレクトリに**.git**フォルダが入った<project-name>フォルダを作成

### 既存のディレクトリをGitリポジトリにする

`$ git init`

カレントディレクトに**.git**フォルダが作成され、Gitリポジトリになる

既存のファイルやフォルダはWorking-areaに追加される

### 既存のリモートリポジトリから作成

fork -> 自分のリモートリポジトリにコピーを作成することができる

forkしたリモートリポジトリをcloneして自分のローカルリポジトリにコピー

fork元にプルリクエストを送ることもできる

# リモートリポジトリ

チームでコードを共有

外部にコードを公開

コードを一元管理する場所

### リーカルリポジトリに設定しているリモートリポジトリを確認

`$ git remote -v`

push先とfetch先がそれぞれ設定されている

### リモートリポジトリから情報を取得する(fetch)

pull = **fetch** + merge

`$ git fetch <remote_ref>`

### fork元のリポジトリにPull Requestを出す

ローカルリポジトリにfork元のリポジトリ情報をセットする

`$ git remote add upstream <repo_url>`

upstream -> このリファレンス名は何でもいいがupstreamとするのが一般的

`$ git remote -v`でリファレンスが作成されたか確認

実際にfork元にpushする場合は、fork元からpullしてくる

`$ git pull upstream <branchname>`


