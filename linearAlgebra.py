import numpy as np

a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

np.matmul(a, b)
print(np.matmul(a, b))

#find the determinant
print("determinant")
c = np.identity(3)
print(np.linalg.det(c))

#transpose
print("transpose")
d = np.transpose(c)
print(d)

#inverse
print("inverse")
e = np.linalg.inv(d)
print(e)

#trace
print("trace")
f = np.trace(e)
print(f)

#eigenvalues
print("eigenvalues")
g = np.linalg.eig(e)
print(g)

#eigenvectors
print("eigenvectors")
h = np.linalg.eig(e)
print(h)

#matrix normalization
print("matrix normalization")
i = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(np.linalg.norm(i))

#singular vector decomposition
print("singular vector decomposition")
j = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(np.linalg.svd(j))

#statistics 
print("statistics")
stats = np.array([[1,2,3], [4,5,6]])
print(stats)

print(np.min(stats))

print(np.max(stats))

print(np.mean(stats))

print(np.median(stats))

print(np.std(stats))

print(np.sum(stats))
