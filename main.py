import numpy as np


print("a")
a = np.array([1, 2, 3])
print(a)

print("b")
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

#get dimensions
print("dimensions")
print(a.ndim)   
print(b.ndim)

#get shape
print("shape")
print(a.shape)
print(b.shape)

#get type
print("type")
print(a.dtype)
print(b.dtype)

#get size
print("size")
print(a.size)
print(b.size)

#get items
print("items")
print(a.itemsize)
print(b.itemsize)

#get total size
print("total size")
print(a.nbytes)
print(b.nbytes)

