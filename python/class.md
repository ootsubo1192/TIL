# class

クラスの継承

```python
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

```

```python
class ToyotaCar(Car):
    pass
```

クラスの中で`Car`を継承しているので`Car`クラスのメソッドを実行できる

```
class TeslaCar(Car):
    def auto_run(self):
        print('auto run')
```

`Car`の継承と`TeslaCar`クラスの中で新たにメソッドを作成しているのでどちらのメソッドも実行することができる
