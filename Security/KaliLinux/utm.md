# UTMインストール

# Kali Linux のインストール

### バージョンアップ
```
sudo apt update
```
```
sudo apt upgrade -y
```
```
sudo apt autoremove -y
```
```
sudo apt autoclean
```

### ユーザーパスワードの変更
```
passwd
```

### ターミナルの操作
タブの追加: 
[Ctrl] + [Shift] + [T]

文字のコピー: 
[Ctrl] + [Shift] + [C]

文字のペースト: 
[Ctrl] + [Shift] + [V]

### ホストキー
ゲストOS内からマウスカーソルが出ない場合に、ホストキーを使用する
[Ctrl] + [Option]

### Kaliの日本語化
```
sudo dpkg-reconfigure locales
```

`jp_JP.UTF-8 UTF`をスペースキーで選択

[Tab]キーでOKを選択して[Enter]キーを押す

`jp_JP.UTF-8 UTF`が見つからない場合

```
sudo apt install task-japanese task-japanese-desktop -y
```
```
sudo update-locale LANG=ja_JP.UTF-8
```

### スリープの変更
[Settings] > [Power Manager] > [Display] > [Blank after]をNeverに変更し、オフに変更

### 共有フォルダ設定
OSを停止した状態で、UTMの画面で[Shared Directory]を設定する

```
sudo mkdir /mnt/utm
```
```
share /mnt/utm 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail,auto 0 0
```

永続化するために、`/etc/fstab`に追記する

```
sudo vim /etc/fstab
```

以下を追加する
```
share /mnt/utm 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail,auto 0 0
```

