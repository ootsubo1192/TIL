# systemd timer

## これは何か
systemd timer は、systemd が提供する機能の一つで、指定した時間に指定したジョブを実行するための機能

cronが今後サポートされなくなる可能性が有り、 代替えとして使用されるもの

[Deprecated in AL2023](https://docs.aws.amazon.com/linux/al2023/ug/deprecated-al2023.html#deprecated-cron)

## 使い方
1. サービスユニットファイルとタイマーユニットファイルを作成
    hoge.service と hoge.timer を作成
2. `etc/systemd/system/`ディレクトリにサービスユニットファイルとタイマーユニットファイルを配置
3.  systemdデーモンを再起動して、タイマーを有効化
    ```
    sudo systemctl daemon-reload
    ```
    ```
    sudo systemctl enable hoge.timer
    ```
    ```
    sudo systemctl start hoge.timer
    ```
4. エラー時のslack通知設定を追加するために、slackのwebhookを取得
5. slack通知用シェルファイル(systemd-slack)と、サービスユニットファイル(status-slack-user@.service)を作成
6. `etc/systemd/system/`ディレクトリにサービスユニットファイルを配置
7. `/usr/local/bin/`ディレクトリにslack通知シェル(systemd-slack)を配置
8.  systemdデーモンを再起動
    ```
    sudo systemctl daemon-reload
    ```

### その他のコマンド
- タイマーの状態確認
    ```
    systemctl status hoge.timer
    ```
- タイマーの一覧確認 オプション: --all
    ```
    systemctl list-timers
    ```
- タイマー停止
    ```
    sudo systemctl stop hoge.timer
    ```
- タイマー無効化
    ```
    sudo systemctl disable hoge.timer
    ```
- ログの確認
    ```
    journalctl
    ```
- タイマー実行時間の確認テスト
    ```
    systemd-analyze calendar "*-*-* 00/2:10:00"
    ```

## 参考
[systemd/タイマー](https://wiki.archlinux.jp/index.php/Systemd/%E3%82%BF%E3%82%A4%E3%83%9E%E3%83%BC)

[Sending messages using incoming webhooks](https://api.slack.com/messaging/webhooks)
[Message payloads](https://api.slack.com/surfaces/messages#payloads)
[Building with Block Kit](https://api.slack.com/block-kit/building)
