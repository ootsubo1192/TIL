# class

## クラスの作成

```python
class Person(object): # (object)は()だけでもいいが書くのがデフォルト
    def __init__(self, name): # コンストラクタ(クラスの初期化)
        self.name = name

    def say_something(self): # (self)と自分自身に値を保持することで関数内で使えるようになる
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self): # デストラクタ(オブジェクトが必要なくなったときに実行)
        print('good bye')


person = Person('Mike')
person.say_something()

del person # 明示的に終了の実行(del文がなかったら最後にデストラクタが実行される)

print('#################')
```

```output
I am Mike. hello
runrunrunrunrunrunrunrunrunrun
#################
good bye
```
