#!/bin/zsh

echo ファイル名を指定してください。

read file_name

touch ${file_name}

# "shiban"を新規作成したファイルに出力
echo "#!/bin/zsh" > ${file_name}

# 権限の変更
chmod 744 ${file_name}

echo 新規スクリプトファイルの作成

