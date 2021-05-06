# decorator

```python
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        resultt = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
```

理解できていない2021/05/07

