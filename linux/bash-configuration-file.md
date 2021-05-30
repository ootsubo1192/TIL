# configuration file

### 全ユーザー

| ファイル名 | 読み込みタイミング | 主な設定内容 |
|:----|:-----|:----|
| /etc/bash.bashrc | bash起動時 | bash起動時に実行させたい処理(Debian系) |
| /etc/bashrc | bash起動時 | bash起動時に実行させたい処理(RedHat系) |
| /etc/profile | ログイン時 | 環境変数、利用環境に関わるもの |

### 各ユーザー個別

| ファイル名 | 読み込みタイミング | 主な設定内容 |
|:----|:-----|:----|
| ~/.bash_profile | ログイン時 | 環境変数などのユーザー環境に関わるもの |
| ~/.bash_login | ログイン時 | ~/.bash_profileがない場合のみ読み込み候補(内容は~/.bash_profileと同じ) |
| ~/.profile | ログイン時 |  | ~/.bash_loginがない場合のみ読み込み候補(内容は~/.bash_profileと同じ)
| ~/.bashrc | bash起動時 | bash起動時に実行させたい処理 |
| ~/.bash_logout | ログアウト時(直前) | ログアウト時に実行させたい処理 |

