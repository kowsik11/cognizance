import numpy as np
a = np.array([1, 4, 7, 5, 6])
print("original array : ")
print(a)
z = 5
Z = np.zeros(len(a) + (len(a)-1)*(z))
Z[::z+1] = a
print("The new array : ")
print(Z)
