# closure

```python
def outer(a, b):
    
    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)
```


```python
def circle_area_fun(pi):
    def circle_area(redius):
        return pi * redius * redius

    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10))
print(cal2(10))
```

