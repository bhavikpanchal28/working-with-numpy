import numpy as np

a = np.array([1,2,3,4])
print(a)

a + 2
print((a+2))

print(a - 2)

print(a * 2)

print(a / 2)

print(a // 2)

print(a ** 2)

b = np.array([1,0,1,0])
print(b)
print(a & b) #AND

print(a | b) #OR

print(a ^ b) #XOR

print(a << 2) #LEFT SHIFT

print(a >> 2) #RIGHT SHIFT

print(a + b) #ADD

np.cos(a)
print(np.cos(a))