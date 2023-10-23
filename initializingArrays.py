
import numpy as np

#all 0s matrix
print("zeros")
a = np.zeros((2,3))
print(a)

#all 1s matrix
print("ones")
b = np.ones((4,2,2))
print(b)

#any other number
print("any other number")
c = np.full((2,2), 5)
print(c)

#any other number (full_like)
print("any other number (full_like)")
d = np.full_like(a, 5)
print(d)

#random decimal numbers
print("random decimal numbers")
e = np.random.rand(4,2)
print(e)

#random integer numbers
print("random integer numbers")
f = np.random.randint(-4,8, size=(4,2))
print(f)

#the identity matrix
print("the identity matrix")
g = np.identity(4)
print(g)

#repeating an array
print("repeating an array")
arr = np.array([[1,2,3]])
h = np.repeat(arr, 3, axis=0)
print(h)

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:-1, 1:-1] = z
print(output)
