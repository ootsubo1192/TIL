# nmcli

Network Managerを管理するためのコマンドラインインタフェース(CLI)

### 書式

`nmcli オブジェクト [コマンド]

## コマンドとオブジェクト(操作する対象)

| オブジェクト | コマンド | 説明 |
|:---|:---|:---|
| general | status | Network Managerの状態を表示 |
| geenral | hostname[ホスト名] | ホスト名を表示、指定したホスト名に変更 |
| networking | {on | off} | ネットワークの有効化|無効化 |
| networking | connectivity | ネットワークの接続状態を表示 |
| radio | wifi | wi-fiの状態を表示 |
| radio | wifi{on|off} | wi-fi接続を有効化|無効化 |
| connection | show | 接続状況の表示 |
|  | modifyID パラメータ | 指定した接続IDの設定ファイルの、指定したパラメータを書き換える。パラメータの反映には接続のconnection up操作が必要 |
