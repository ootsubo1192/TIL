# network file

ネットワーク関連の設定ファイルの名前と内容


| ファイル名 | 設定内容 | 表示例 |
|:---|:---|:---|
| /etc/hostname | ホスト名を設定(Debian系) | cat /etc/hostname <br>Debian |
| /etc/sysconfig/network | ホスト名を設定(RedHat系)ネットワーク機能の有効・無効。デフォルトゲートウェイ等も設定可 | cat /etc/sysconfig/network <br>NETWORKING=yes <br>HOSTNAME=CentOS <br>GATEWAY=192.168.1.1 |
| /etc/hosts | IPアドレスとホスト名の対応付け | cat /etc/hosts<br>112.78.124.10 ping-t.com<br>192.168.1.100 FileServer |
| /etc/nsswitch.conf | 名前解決やサービス名解決の際の問い合わせ順序を指定 | cat /etc/nsswitch.conf<br>hosts: file dns<br>services: files |
| /etc/resolv.conf | ドメイン名やDNSサーバの指定 | cat /etc/resolv.conf<br>domain ping-t.com<br>nameserver 192.168.1.1 |
| /etc/services | サービス名とポート番号の対応付け | cat /etc/services<br> telnet 23/tcp |


