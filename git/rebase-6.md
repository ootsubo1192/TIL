# rebase

mergeとrebaseの違い

merge -> マージコミットが作られて、親コミットが2つある状態になる

rebase -> マージコミットが作られず、親コミットを1つにしてコミット履歴をスッキリさせることができる

将来マージするブランチを適宣rebaseしておくとことで、後々マージしやすくなる

既存のコミットを**削除**して、新たなコミットを作成

**一度push済みのコミットをrebaseはしない**

自分のローカルリポジトリでのみrebaseをつかう

---

rebase元にしたいブランチの移動してrebase

`$ git rebase master`

masterブランチにrebase元のブランチを統合

### コンフリクトへの対応

コンフリクトをmergetoolで対処

rebaseが途中で中断しているので

`$ git rebase --continue`

### pull時にmergeではなくrebaseする

`$ git pull --rebase <remote_ref> <branchname>


