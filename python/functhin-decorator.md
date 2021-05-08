# decorator

```python
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        pritn('kwargs:', kwargs)
        resultt = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        resultt = func(*args, **kwargs)
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

`f = (print_info(print_more(add_num)))`

上の関数の簡単なイメージ

理解できていない2021/05/07

