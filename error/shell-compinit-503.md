# source <FILENAME> error

`source .zshrc` -> ファイルを更新したので実行したかったが以下のエラーになる

`compinit:503: no such file or directory: /usr/local/share/zsh/site-functions/_brew_cask`

何故かそのようなファイルやディレクトリーはないとえらーになるの

```zsh
brew cleanup
```

```
Warning: Skipping autoconf: most recent version 2.71 not installed
Warning: Skipping openssl@1.1: most recent version 1.1.1k not installed
Warning: Skipping pkg-config: most recent version 0.29.2_3 not installed
Warning: Skipping pyenv: most recent version 1.2.24.1 not installed
Warning: Skipping readline: most recent version 8.1 not installed
Pruned 6 symbolic links from /usr/local
````

"brew"が悪さをしていたのかクリーンアップすることで実行できるようになった

date 2021/05/04

