# uniquely exception

## 独自例外の作成

```python
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
```

`class <NAME>(Exception):` -> "Exception"の内容を継承して別名をつけるイメージ

`pass` -> 単純に"Exception"を実行する

もし"words"に大文字の文字列が含まれていた場合にエラーを出す

**例外名に既存のエラーネームを使用しない**

