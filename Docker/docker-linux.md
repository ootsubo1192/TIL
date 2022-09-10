# Dockerを使用してLinux環境を構築し学習できるようにと思い、Dockerでの環境構築についてまとめていきます。  
## AWS EC2 インスタンスを作成すれば、簡単に環境構築できますが、コンテナ技術も併せて学習してみてください。
### 本内容はMacを対象に作成しています。  

目次
1. Dockerhubへの登録とDocker Desktopのインストール
2. 



Dockerhubへの登録  
DockerhubはDocker image というものを管理する場所(レジストリ)になります。
"https://hub.docker.com/"に接続してください。  
"DockerID" "Email" "Password" を登録する画面になるので、入力してください。  
"DockerID" は、自身のDocker imageの保存先になるURLの一部になるので注意してください。
後で変更できないわけではないですが、面倒な手順を踏む必要があります。  
Dockerhub にサインインすると、確認用のメールが送られてくるので、メールアドレスに間違いがないことを確認してください。  
Dockerhub にログインすると、Docker Desktop のダウンロードページになるのでダウンロードしてインストールしてください。

ターミナルからコマンドでDockerへログインする。  
$ Docker login
  Username:
  Password:
"Username"はDockerhubに登録した"DockerID"になり、"Password"はDockerhubの"Password"になります。  

コンテナの起動
$ docker run -it <ContainerID> bash

コンテナの削除
$ docker rm <ContainerID>  
コンテナが"Exited"状態のものしか削除できない  
コンテナの全削除
$ docker system prune  
すべての"Exited"状態のコンテナを削除する。  

コンテナの停止  
$ docker stop <ContainerID> <ContainerID>
一度に複数停止することも可能  

Dockerfile から Docker image を作成する。
Dockerfile というファイル名は固定する  
ディレクトリ内には一つの Docerfileを作成する  

$ docker build <directory>  

Dockerfile があるディレクトリに移動して、コマンドを実行することを推奨する。  

$ docker build .  

タグ付け

$ docker build -t <repository-name>:<tag> .  

