# set comprehensions

集合内包表記

```python
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0)}
print(s)
print(type(s))
```

```output
{0, 2, 4, 6, 8}
{0, 2, 4, 6, 8}
<class 'set'>
```

ほとんどリスト内包表記と同じ

