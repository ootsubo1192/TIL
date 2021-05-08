# decorator

関数を入れ子構造にして実行

```python
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        pritn('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        print('##############')
        result = func(*args, **kwargs)
        print('##############')
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
```

```output
start
##############
func: add_num
args: (10, 20)
kwargs: {}
result: 30
##############
end
30
```

```python
@print_info
@print_more
```

この順番は重要、これを逆にすると出力結果も変わってくる

`f = (print_info(print_more(add_num)))`

上の関数の簡単なイメージ

`def print_info`の`result = func()`が実行されると`def print_more`に移動するんだが理解できない


理解できていない2021/05/07

