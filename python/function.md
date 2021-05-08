# function

関数定義の基礎構文

```python
def day_something():
    print('hi')

f = say_something
f()
```

`def`の後に関数名を定義して()で閉じる、その後に関数内でやりたいことの定義

`f`に`say_someting`関数を代入して、`f()`で出力


---

```python
def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)
```

`s`に出力したいことを代入して、`return`で出力

`result`に関数を代入して`print(result)`で出力

---

データ型の指定(指定するだけで構文でのエラーにできるわけではない)

```python
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a' + 'b')
print(r)
```

`a: int`で数値を入れてと指定、`-> int:`で出力も数値型になりますと教えてくれる

基本的に使わない、文字列を入れたからと言ってエラーにもならない

----

関数のデフォルト引数にリストや辞書型の参照渡しになるものを置かない(バグにつながる)

```python
def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)
print(id(r))

y = [1, 2, 3]
r = test_func(200, y)
print(r)
print(id(r))

r = test_func(100)
print(r)
print(id(r))

r = test_func(100)
print(r)
print(id(r))
```

```
[1, 2, 3, 100]
4454848256
[1, 2, 3, 200]
4455127616
[100]
4454824960
[100, 100]
4454824960
```

参照渡しになる空のリストを使うことで最後のプリント分に前の関数の出力結果まででてくる

IDも同じなので同じメモリから出力されている

バグの元なので引数に用いない

以下のように書くことでバグを回避する

```python
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
```

もし`l`に何も指定がなかったときだけ関数内で空のリストを生成

こうすることで別のメモリにリストが作られ重複が避けられる

---


