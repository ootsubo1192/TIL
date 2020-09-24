# GitHub Flow の流れ

masterブランチからブランチ作成

```bash
$ git checkout -b <ブランチ名>
$ git branch <新規ブランチ名>
```
ブランチを作成、変更したら
ファイルの修正、追加
ローカルリポジトリにコミット

```bash
$ git add <ファイル名>
$ git commit -m <変更内容の記述>
$ git push origin <現在のブランチ名>
```
現在のブランチ＝＝新規ブランチ

GitHub上にプルリクエストが作成される
Pull requests
New pull request
base: master   compare: <新規ブランチ>
Create pull request
タイトル、内容の作成
Create pull request

レビューの依頼
Reviewersから依頼

レビューワー側がすること
Files changed から変更内容の確認
緑が追記、　赤が削除
問題なければ　Review changes
Approve > Submit review

Conversation > Merge pull request
Confirm merge 
Delete branch

マスターブランチをデプロイ

ブランチの後片付け

```bash
$ git checkout master
$ git pull origin master
$ git branch -d <新規ブランチ名>
```



