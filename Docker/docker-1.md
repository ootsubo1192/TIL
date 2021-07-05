# docker 

`$ docker login`

DockerHubに登録してた情報の入力

`$ docker pull <image>

DockerHubにあるイメージの取得

`$ docker images`

Dockerに作成したリポジトリの一覧表示

`$ docker run <image>

イメージからコンテナの作成

`$ docker ps`

現在実行中のコンテナの一覧表示

`$ docker ps -a`

アクティブではないコンテナも含めてすべて表示

`$ docker restart <conteinerID>`

コンテナの再起動

`$ docker exec <containerID> <command>`

コンテナの中に入る

`$ exit`

コンテナから抜ける(コンテナはUP状態のまま)

`$ docker commit <container> <new image>`

コンテナから新たにイメージを作成する

`$ docker push <username>/<repository>:tagname`

DockerHubのレポジトリにイメージを上げる

1つのイメージに対して1つのレポジトリを作成する

イメージの名前をレポジトリ名と合わせる必要がある

`$ docker tag <source> <target>`

`$ docker tag ubuntu:updated <username>/<repository>`

---

`$ docker tag <imageID> <username>/<repository>`

イメージを上書きすることができる

`$ docker rmi <image>`

イメージの削除

### docker run について

イメージの作成とイメージの起動を同時に行う

run = create + start

`$ docker create <image>`

イメージの作成

`$ docker run <image>`

イメージの起動

### コマンドの上書き

イメージを起動するとイメージのデフォルトのコマンドが実行される

起動時にコマンドを入力するとコマンドが上書きされて実行される

`$ docker run -it ubuntu <command>`

-i -> インプット可能にする

-t -> 表示が綺麗になる

### コンテナの削除

`$ docker rm <containerID>`

コンテナの削除(コンテナ名でも可能)

起動状態のコンテナは削除することができない

`$ docker stop <containerID>`

コンテナを停止する(Exited状態にする)

`$ docker system prune`

停止中のコンテナをすべて削除

### コンテナに名前をつける

起動させ続けるコンテナを立てたり、共有サーバで使用するときなど

`$ docker run --name <name> <image>`

### detachedモード

`$ docker run -d <image>

コンテナを起動後にdetachする(バックグラウンドで起動)

### foregroundモード

`$ docker run -rm <image>

コンテナをExit後に直ぐに削除する(1回きりのコンテナを作成、コンテナがたまらない)

### buildコマンドのオプション

`-v <host>:<container>` -> ホストのファイルシステムをコンテナにマウントする

フォルダが無いときは自動的に作られる

`-u $(id -u):$(id -g)` -> ユーザーIDとグループIDを指定してコンテナを作成

`-p <host_port>:<container_port>` -> ホストのポートをコンテナのポートに繋げる

Webサービスをコンテナに作成した時にホストのポートをWebサービスに接続するために使用

--cpus <# of CPUs> -> コンテナがアクセスできる上限のCPUを設定

--memory <byte> -> コンテナがアクセスできるメモリを設定

`$ docker inspect <container>` -> コンテナのあらゆる情報を一覧表示できる

### イメージを圧縮

`$ docker save <image> > <filename>.tar`

