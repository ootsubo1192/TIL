# Dockerfile

基本的にDockerfileを作成してイメージを作成しコンテナを起動する

**Dockerfile**という名前のテキストファイル(ファイル名の頭文字は大文字で記載！大文字にしないとDockerが認識しない、オプションをわざわざ書く必要が出てくる)

docker build -f <dockerfilename> <build context>`

Dockerfileがbuild contextに入っていない場合

Dockerfileとbuild contextを分けて管理することがある

ファイル内は**INSTRUCTION arguments**の形式で記載

`$ docker build .`

Dockerfileからイメージの作成

`$ docker build --platform linux/amd64 .`

M1mac用のコマンド

### build context

Dockerdaemonがbuild context(フォルダ)からイメージを作成

build contextの中には余計なファイルは置かない(ビルドに余計な時間がかかるため)

イメージにDockerfile以外が入る訳ではないので、イメージサイズには影響しない

## INSTRUCTION

**FROM** -> ベースとなるイメージを決定、DockerfileはFROMから書き始める

**RUN** -> Linuxコマンドの実行、RUN毎に**イメージLayer**が作られる

---

Docker image のLayer数は最小限にする

LayerはRUN,COPY,ADDで作られる

コマンドを**&&**でつなげたり、**\**で**改行してRUNを一度にまとめる

バッケージの追加には新たにRNUを作って、元のパッケージはキャッシュを使ってビルド時間を短くする

---

**CMD** -> コンテナのデフォルトのコマンドを指定

`CMD ["executable", "param1", "param2"]`

原則的に最後に記載

**ENTRYPOINT** -> run時に上書できないデフォルトのコマンドを指定する

ENTRYPOINTがDockerfileにある場合は、CMDにはENTRYPOINTの引数を記載していく

run時に引数のみ上書きされると覚える

**COPY** -> build context内のファイルをイメージに反映させる

**ADD** -> tarの圧縮ファイルをコピーして解答(build contextのファイルやフォルダを圧縮して、ビルド時間を短縮する事ができる)

**ENV** -> 環境変数を指定する

**WORKDIR** -> Docker instructionの実行ディレクトリを変更

コマンドはroot直下で実行されるので実行ディレクトリを変更する必要がある

RUNでcdコマンドを使用しても意味がない

pathは絶対パスで記載するとわかりやすい

### RUN vs CMD

RUNはLayerを作るが、CMDは作らない


