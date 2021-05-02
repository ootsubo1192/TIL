# input and output

"cat" コマンドを使ったインプットとアウトプット

### standard output

`cat 1> output.txt` -> "output.txt"というファイルに文字列を上書き出力、入力が終わったら`Ctrl-c`で終了

`cat 1>> output.txt -> "output.txt"に追加して出力

### standard error

`cat 2> error.txt` -> "error.txt"ファイルにエラーのみを上書き出力

`cat 2>> error.txt` -> "error.txt"に追加して出力

### standard input

`cat 0< output.txt` -> "output.txt"ファイルの内容をインプットして表示

`cat 0< output.txt 1> hello.txt` -> "output.txt"ファイルの内容を"hello.txt"ファイルに出力みたいなこともできる


