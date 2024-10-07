# CUPS(Common UNIX Printing System)

ネットワーク上のプリンタをサポートするプロトコルとして[IPP(Internet Printing Protocol)]を採用

プリンタの機種依存情報を記述するファイルとして[PPD(Postscript Printer Description)]がある

標準的な印刷コマンド

| lp | 印刷ジョブを生成し、プリントキューに登録 |
| cancel | プリントキューにある印刷ジョブを削除 |
| lpstat | プリントキューにある印刷ジョブを表示 |

レガシーなコマンド

| lpr | 印刷ジョブを生成し、プリントキューに登録(r -> registry(登録)) |
| lprm | プリントキューにある印刷ジョブを削除(rm -> remove) |
| lpq | プリントキューにある印刷ジョブを表示(q -> queue) |

## lpr

プリントキューに印刷ジョブを登録し、指定したファイルを印刷するコマンド

### 書式

`lpr [オプション] [ファイル名]`

### オプション


| -#数 | 指定した部数を印刷 |
| -Pプリンタ名 | してしたプリンタに出力 |

- プリンタの指定をしなければ、デフォルトのプリンタで印刷する

- lpd /var/log/messages -> Liunxでこれまで利用されてきた印刷用のデーモンプログラム。

例) lpr -PPrinterA /etc/group -> /etc/groupファイルをPrinterAで印刷
