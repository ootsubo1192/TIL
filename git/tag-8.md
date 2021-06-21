# tag

`$ git tag <tagname>` -> 最新のコミットにラベル付けする

特定のコミットを特定のversionとして公開したりするのに使う(マイルストーン)

git log でtag名も履歴とともに表示される

`$ git tag --list` -> tagの一覧を表示する

`$ git tag --delite <tagname>` -> 指定したtagを削除する

### tagにアノテーション(追加情報)をつける

`$ git tag -a <tagname>`

基本的にバージョン管理用に追加情報をつけたtagを作る

`$ git tag -a -m "message"` -> エディタを開かずにアノテーションを書く

### tag同士のdiffを表示

`$ git diff <tagname1> <tagname2>` -> 左側にbaseを置く(古いtag)

### 特定のコミットにtag付け

`$ git tag -a <tagname> <commitID> 

### リモートリポジトリにtag情報を送信

`$ git push <remote_ref> <tagname>` -> 指定のtagをリモートリポジトリに送信

git pushするだけだとtag情報はpushされない(tagでのバージョンを公表するかは、慎重に行う必要があるため)

`$ git push <remote_ref> --tags` -> すべてのtag情報をpushする

`$ git push <remote_ref> :<tagname>` -> 特定のtag情報をリモートリポジトリから削除する

また開発中でtag情報を付けたくない場合

### 特定のtagで作業する

`$ git checkout tags/<tagname>` -> コードを特定のバージョンの状態にする

`$ git fetch --tags --all -> すべてのtag情報をローカルに取得

もし上のcheckoutコマンドで変更できなければ、一度tag情報をfetchするといい


