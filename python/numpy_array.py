import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array1)
array1.shape  # (3, 3)

# いろいろな次元
a = np.expand_dims(array1, axis=0)
print(a)

a.shape	# (1, 3, 3)

b = np.expand_dims(array1, axis=1)
print(b)
b.shape # (3, 1, 3)

c = np.expand_dims(array1, axis=2)
print(c)
c.shape # (3, 3, 1)


