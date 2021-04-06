# \*args and **kwargs

### \*args

```python
def func(*args)
    return args[0] + args[1]
```

\*argsの中にいくつでも引数を入れることができる
引数は`Tuple`で返される。

引数名は何でもいいが、わかりやすいように`args`にする

### \*kwargs

```python
def print_dict(**kwargs)
    param_a = kwargs.get('a', 100)
    param_b = kwargs.get('b', 200)
    print(param_a)
```

`dict`型で引数を入れることができる
引数名は何でもいい、わかりやすいように

