# for

## zip

```python
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['cook', 'tea', 'water']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
```

```
Mon apple cook
Tue banana tea
Wed orange water
```

"zip" で複数のリストをまとめて "for"　文で回す

## range

```python
for _ in range(10):
    print('hello')
```

"range" 関数で1~10まで関数をループさせる( _ を使うことでrange関数からのindex番号は出力に使われないと表明できる)

## enumerate

```python
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
```

"i"にindex番号を入れて同時に出力

## dict

```python
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)
```

"items"を使用することでリスト型にしてfor文で回し、unpakkingすることでキーとバリューを出力している

