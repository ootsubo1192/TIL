# nmcli

Network Managerを管理するためのコマンドラインインタフェース(CLI)

### 書式

`nmcli オブジェクト [コマンド]`

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
| connection | modifyID パラメータ | 指定した接続IDの設定ファイルの、指定したパラメータを書き換える。パラメータの反映には接続のconnection up操作が必要 |
| connection | {up | down} ID | 接続の有効化|無効化 |
| device | status | デバイスの状態を表示 |
| device | show インタフェース名 | 指定したデバイスの詳細情報を表示 |
| device | {connect | disconnect} インタフェース名 | 指定したデバイスを接続|切断 |
| device | modify インタフェース名 パラメータ | 指定したインタフェースのパラメータを即時変更する。指定ファイルの書き換えは行われない |
| device | monitor インタフェース名 | 指定したデバイスの監視 |
| device | delete インタフェース名 | ソフトウェアデバイス(ブリッジなど)の削除 |
| device | wifi list | Wi-Fiアクセスポイントの表示 |
| device | wifi connect SSID | Wi-Fiに接続するデバイスを作成、有効化|
| device | wifi rescan | Wi-Fiアクセスポイントの再検索 |

