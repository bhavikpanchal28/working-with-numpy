import numpy as np

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

# cant do this because it is a 2d array
# after = before.reshape((2,3))


after = before.reshape((2,2,2))
print(after)

#vertically stack vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack((v1, v2, v1, v2)))

#horizontally stack vectors
h1 = np.ones([2,4])
h2 = np.zeros([2,2])

print(np.hstack((h1, h2)))

