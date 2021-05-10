# class

## クラスの継承

```python
class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car): # class Carを継承、継承しない場合は(object)を明示的に書く
    pass

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model) # "class Car"の"__init__"を継承する
        self.enable_auto_run = enable_auto_run # "TeslaCar"の中だけで定義
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar('Model S')
tesla_car.run()
tesla_car.auto_run()

```

