
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

#get a specific element [row, column]
print(a[1, 5])

#get a specific row
print(a[0, :])

#get a specific column
print(a[:, 2])

#get a little bit more fancy [startindex:endindex:stepsize]
print(a[0, 1:-1:2])

a[1,5] = 20
print(a)

a[:, 2] = [5, 6]
print(a)

#replace
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

print(b)