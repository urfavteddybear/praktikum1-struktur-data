import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 2])

# perulangan array 3d
var = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in var:
 for y in x:
  for z in y:
   print(z)

# perubahan isi array ke N
var1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(var1[0, 1, 2])
var1[0][1][2] = 30;
print(var1[0, 1, 2])
