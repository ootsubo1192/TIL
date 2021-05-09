# gererator comprehensions

ジェネレーター内包表記

```python
def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

t = tuple(i for i in range(10) if i % 2 == 0)
print(type(t))
print(t)
```

```output
<class 'generator'>
0
2
4
6
<class 'tuple'>
(0, 2, 4, 6, 8)
```

"()"で囲んだだけだとジェネレーター型

”tuple()”とすることでタプル型にできる

