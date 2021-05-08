# Lambda function

通常の関数の書き方

```python
def func(a):
    return a + 1
```

lambda 記法

```python
lambda a: a + 1
```

余計なものはすべて取る
`(def, 関数名, return, 改行, カッコ)`

名前も付ける必要がない簡単な関数の作成時に使用する。

## labda 2

```python
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))
        

def sample_func(word):
    return word.capitalize()


change_words(l, sample_func)
```

実行順 35->27->28->32->28->27->以下リスト`l`の最後まで

```output
Mon
Tue
Wed
Thu
Fri
Sat
Sun
```

