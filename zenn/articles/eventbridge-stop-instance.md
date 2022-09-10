---
title: "AWS EventBridgeを使用し、EC2インスタンの停止を通知"
emoji: "🐔"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: [ "aws", "EventBirdge", "AWS CLI"]
published: false
---


# AWS EventBridge と Amazon SNS を使用して、EC2インスタンの停止をEメー通通する。

構築済みのEC2インスタンが停止したことを受けて、EventBridgeのイベン駆動でSNSからEメールを送信して通知してみたと思う。

前半では、AWSコンソールから作成し、後半で同じ構成をAWS CLIを使用して作成してみる。

EventBridgeのターゲットとしてSNSトピックを指定する必要があるので、先にSNSトピックの作成と、サブスクリプションでEメールアドレスを登録していく。

### SNS トピックを作成

まずは「SNSを作成」を選択

次に「名前」と「表示名」を入力していく。

表示名を入力することで、Eメール通知の件名になる。

![](https://storage.googleapis.com/zenn-user-upload/ff19cdc10166-20220910.png)

