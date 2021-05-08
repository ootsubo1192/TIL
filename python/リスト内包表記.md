# List Comprehensions

以下のリストに`.png`をつけたいとします。

`color = ['red', 'blue', 'green', 'yellow', 'white']`

```python
for color in colors:
  color_png = color + 'png'
  color_png.append(color_png)
```

`colors_png = ['red.png', 'blue.ong', 'green.png', 'yellow.ong', 'white.png']`
が出力される

これをリスト内包表記で書く

```python
[ color + '.png' for color in colors]
```

## example 

```python
t = [1, 2, 3, 4, 5]
t2 = [5, 6, 7, 8, 9, 10]

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]
print(r)
```

"for"文1つに"if"文1つくらいが読みやすく最適

```output
[2, 4]
[2, 4]
```

```python
t = [1, 2, 3, 4, 5]
t2 = [5, 6, 7, 8, 9, 10]

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]
print(r)
```

"for"文を2つも3つの続けると可読性が悪くなりバクにもつながる


