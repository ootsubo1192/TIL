## pythonのrange関数

Pythonで連番や等差数列を作成してfor文で使ったり、リストを取得するのに使う
等差数列：同じ数ごと増える(減る)数列

```python
print(range(3))
#range(0, 3)
#printで出力しても表示されない。イテラブルなのでfor文で回せる

```
```python
for i in range(3):
	print(i)
# 0
# 1
# 2
```
リストで作成することも可能
```python
print(list(range(3)))
# [0, 1, 2]
```
可視化しやすくしているだけなので、通常はfor文でいい

```python
range(stop)
#指定がない場合stop-1,step=1の数列

print(list(range(start, stop, step)))

print(list(range(1, 4)))
# [1, 2, 3]

print(list(range(-3, 1)))
# [-3, -2, -1, 0]

print(list(range(1, 10, 3)))
# [1, 4, 7]

print(list(range(10, 1, -3)))
# [10, 7, 4]
```
rangeの引数に指定できるのは整数 int のみ
float は指定できない

どうしてもfloatで等差数列を作成したい場合はリスト内包表記
```python
print(i / 10 for i in range(3, 10, 2))
# [0.3, 0.5, 0.7, 0.9]
```
Numpyの np.arange()を使うほうが簡単
```python
import numpy as np

print(np.arange(0.3, 1.0, 0.2))
# [0.3, 0.5, 0.7, 0.9]
```
