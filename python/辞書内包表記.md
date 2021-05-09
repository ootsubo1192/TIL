# 辞書内包表記

"for"文の簡略化

```python
week = ['mon', 'tue', 'wed']
drink = ['coffee', 'milk', 'water']

f = {}
for x, y in zip(week, drink):
    d[x] = y

print(f)

f = {x: y for x, y in zip(week, drink)}
print(f)
```

```output
{'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}
{'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}
```


