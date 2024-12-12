# Error

## Shada file error
```
function nerdtree#ui_glue#invokeKeyMap[1]..76[18]..75[3]..<SNR>31_customOpenFile[1]..105[1]..121[3]..177[6]..178[17]..13 の処理中にエラーが検>
出されました:
line    3:
E576: Error while reading ShaDa file: last entry specified that it occupies 108 bytes, but file ended earlier
続けるにはENTERを押すかコマンドを入力してください
```

- action: Delete shada file

```
rm ~/.local/state/nvim/shada/*
```

[ref](https://github.com/neovim/neovim/issues/12101)

