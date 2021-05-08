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

