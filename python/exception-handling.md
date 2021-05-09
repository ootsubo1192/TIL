# exception handling

例外処理

```python
l = [1, 2, 3]
i = 5

try:
    l[0]
except:
    print("Don't worry")
```

`try`で定義したものにエラーが起きたら

`except`でエラーの処理を行いプログラムが停止しない

```python
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}.format(ex))
else:
    print('done')
finally:
    print('clean up')
```

それぞれのエラーに対して処理を実行できる

`else`で何もエラーが起きなかったときに実行

`finally’で必ず実行される

## Exception hierarchy

例外処理のツリーがリンク先の一番下にあります

[exception hierarchy](https://docs.python.org/3/library/exceptions.html)


