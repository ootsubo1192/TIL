# stash

Working directoryとStaging areaの作業を一時退避させる

---

`$ git stash` -> Working directoryの内容をstashする(`$ git stash`でstashされるのはtrack済みのファイルのみ)

`$ git stash list` -> stashの一覧を表示する

`$ git stash apply` -> stashした内容を戻す

`$ git stash drop` -> applyしたあともstashにはデータが残っているので削除する

stashはデータをスタック構造で保存(後入れ先出し)

`$ git stash -u -> untrackファイルの作業内容も含めてstashする

`$ git stash show stash@{i}` -> 特定のstash内容を表示する(untrackファイルは表示されない)

`$ git stash pop -> 最新のstash内容をpop(戻す)する。applyとdropを同時に行う

`$ git stash -a -> gitignoreしているファイルの作業内容もstash

### 複数の作業内容をstashする

`$ git stash save "<message>"` -> stashする際にメッセージを添える

`$ git stash apply stash@{i}` -> 特定のstashだけをWorking directoryに戻す

`$ git stash drop stash@{i}` -> 特定のstashだけをdropする
：
