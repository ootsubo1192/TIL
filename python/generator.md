# generator

"for"文のように一気に回すのではなく、1つずつ生成していき、途中に他の処理を入れることも可能

```python
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g =greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
```

```output
Good morning
run
run
run
run
run
Good afternoon
run
run
run
run
run
Good night
```

`yield`-> 出力値の生成(どこまで生成したかは記憶されている

`next` -> 次の`yield`の呼び出し

次の呼び出せる`yield`が無くなったら**Stop Iteration**というエラーが返される

