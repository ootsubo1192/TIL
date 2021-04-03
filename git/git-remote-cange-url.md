# Git remote のURLの変更方法

まずは現在のリモートURLを確認方法

```bash
$ git remote -v
```

続いて新しいリモートURLに変更していきます。
GithubのWebページからクローン元のURLをコピー
元のGit remote URLを <dt>ssh</dt> か　<dt>https</dt>　か確認しておく。

```bash
$ git remote set-url origin <newURL>
```

最後にURLを再度確認しておきます。