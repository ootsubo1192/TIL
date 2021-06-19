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


