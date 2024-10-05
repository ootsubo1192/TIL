# fzf

## インストールと初期設定
- [git からインストール](https://github.com/junegunn/fzf)
```sh 
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```
- インストールの選択は`y`で全部OK(3回)
- zshrcの再読み込み
```sh
source ~/.zshrc
```
- vim-plugでプラグインとしてインストール
```
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
```
- vim内で`:PlugInstall`を実行
- ファイル内検索もしたいので`ripgrep`もインストール
```sh
brew install ripgrep
```

## How to use

fzfで検索してEnterを押した場合には、標準出力に出力される。
そのため、他のコマンドと組み合わせることで様々な便利なワンライナーを作成することが可能。

### fzf
- `Ctrl + t`でファイル検索
- `Ctrl + r`でコマンド履歴検索
- `vim ** + Tab `でファイル検索してvimで開く

### fzf.vim
- `:Files`でファイル検索
- `:Rg`でファイル内検索
- `:Windows`でウィンドウ検索

---

**便利なコマンドを随時追加していく**
