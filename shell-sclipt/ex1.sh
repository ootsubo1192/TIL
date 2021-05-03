#!/bin/zsh

# テキストファイルの新規作成と名前の変更の実施

# ファイルの新規作成
touch 1.txt

echo ファイル名を指定してください
# 変数の入力
read name

# ${name}"で変数の出力して"mv"でファイル名の変更"
mv 1.txt ${name}.txt
echo 終了します。


