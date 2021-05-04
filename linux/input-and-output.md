# input and output

入力、出力とエラー出力はそれぞで独立したもの


### standard output

#### **1**は省略可能

`<COMMAND> 1> output.txt` -> "output.txt"というファイルに`cat`の結果を上書き出力

`<COMMAND> 1>> output.txt -> "output.txt"に追加して出力

### standard error

#### **2**は省略できない

`<COMMAND> 2> error.txt` -> "error.txt"ファイルにエラーのみを上書き出力

`<COMMAND> 2>> error.txt` -> "error.txt"に追加して出力

### standard input

#### **0**は省略可能

`<COMMAND> 0< output.txt` -> "output.txt"ファイルの内容をインプットして表示

`<COMMAND> 0< output.txt 1> hello.txt` -> "output.txt"ファイルの内容を"hello.txt"ファイルに出力みたいなこともできる


