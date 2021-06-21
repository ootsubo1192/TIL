# submodule

プロジェクトの一部として別のプロジェクトを使用する

DokerやCICD関連のスクリプトをbaseプロジェクトのように使うこともある

`$ git submodule add <submodule_url> -> プロジェクトにsubmoduleを追加

### .gitmodulesファイル

.gitmodulesファイルにsubmoduleのURLとローカルのpathをマッピングする

submoduleコマンドを打つと作成される

### submoduleを含むプロジェクトをcloneする

submodule以下のファイル／フォルダはcloneされないので注意する

以下のコマンドはsubmoduleフォルダ内で実行する

`$ git submodule init` -> submoduleの初期化(**init**ialize)する

`$ git submodule update -> submoduleの更新(update)する

### clone時にsubmoduleを初期化、更新する

`$ git clone --recurse-submodules <url>` 

cloneする段階でsubmoduleを含んだプロジェクトであることが分かる場合に使用

複数のsubmoduleを含むプロジェクトの場合に楽

リポジトリのREADMEに手順として書いておくと親切

### submoduleが更新された

親プロジェクトのsubmoduleディレクトリは固定のコミットを指しているので、更新する必要がある

submoduleでpullすることによってコミットポインタが更新される

`$ git submodule foreach '<command>'` -> すべてのsubmoduleでコマンドを実行

`$ git submodule foreach 'git pull origin master' -> すべてのsubmoduleで`git pull origin master`を実行

