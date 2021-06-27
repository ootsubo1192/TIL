# Dockerfile

基本的にDockerfileを作成してイメージを作成しコンテナを起動する

**Dockerfile**という名前のテキストファイル(ファイル名の頭文字は大文字で記載！大文字にしないとDockerが認識しない、オプションをわざわざ書く必要が出てくる)

ファイル内は**INSTRUCTION arguments**の形式で記載

`$ docker build .`

Dockerfileからイメージの作成

`$ docker build --platform linux/amd64 .`

M1mac用のコマンド

## INSTRUCTION

FROM -> ベースとなるイメージを決定、DockerfileはFROMから書き始める

RUN -> Linuxコマンドの実行、RUN毎に**イメージLayer**が作られる

---

Docker image のLayer数は最小限にする

LayerはRUN,COPY,ADDで作られる

コマンドを**&&**でつなげたり、**\**で**改行してRUNを一度にまとめる

バッケージの追加には新たにRNUを作って、元のパッケージはキャッシュを使ってビルド時間を短くする

---

CMD -> コンテナのデフォルトのコマンドを指定

`CMD ["executable", "param1", "param2"]`

原則的に最後に記載

### RUN vs CMD

RUNはLayerを作るが、CMDは作らない


