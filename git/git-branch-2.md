#　ブランチ

### ブランチの一覧を表示(現在の作業ブランチを確認)

`$ git branch`

なんのためのブランチなのかわかり易い名前にする

長すぎる名前をつけない

単語を繋げる場合は**-**でつなげる

### 新しいブランチの作成

`$ git branch <branch-name>`

### 作業するブランチを切り替える

`$ git checkout <branch-name>`

### ブランチの作成と切り替えを同時に行う

`$ git checkout -b <branch-name>`

## pagerを無効にする

`$ git config --global --replace-all core.pager "less -F -X"`

`git branch`や`git diff`時にpagerで表示されないようにする(設定済み)

### 特定のブランチの削除

mainブランチにマージしたあとは不要になるので削除

`$ git branch -d <branch-name>`

mainブランチにマージしていないブランチは削除できない

強制削除は`-d`の代わりに`-D`オプションを使用

リモートリポジトリのブランチはGithub上のBranchesで選択肢ゴミ箱マークを押下

### ブランチ名の改名

`$ git branch -m <branchname> <new-branchname>`


