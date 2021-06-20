# diff

ファイルの差分

通常マージする前に差分を確認して、問題がなければマージする

特にmainブランチへのマージの前には、Pull Request上でdiffを確認しておく

### Working directoryとSterging-areaのdiff

`$ git diff/difftool`

difftoolを使用する場合は設定とダウンロードが必要(p4merge)

### Working directoryとローカルリポジトリのdiff

`$ git diff HEAD`

HEADはアクティブブランチの最新のコミットを指すポインタ

### Staging areaとローカルリポジトリのdiff

`$ git diff --staged HEAD`

--staged -> 比較対象をStaging areaにする

### 特定のファイルのdiff

`$ git diff -- <filename>`

-- -> その後に来るものがファイル名だとわかるように(スペースを忘れずに)

### commit同士のdiff

`$ git diff <commitID> <commitID>`

左がbase

基本的に古いコミットを左に、新しいコミットを右に

最新のコミットポイントにはHEADを使う

`$ git diff HEAD^ HEAD`

HEAD^ -> HEADの親コミット

HEAD^^ -> HEADの親の親コミット

親が2つある場合は、^1 ^2と指定する

### ブランチ同士のdiff

`$ git diff <branchname> <branchname>

ブランチはコミットポイントを指すポインタに過ぎないので、コミット同士のdiffと同じと考える

### mergetoolを使ってコンフリクトに対処してマージ

`$ git mergetool`

コンフリクトが起きた際に、エディタではなくdifftoolを開いてコンフリクトの解消を行う

コンフリクトを解消すると新たに**.orig**というファイルが作成される

difftoolが勝手に作る、オリジナルのファイル(untrackファイルなのでrmコマンドで削除していい)

