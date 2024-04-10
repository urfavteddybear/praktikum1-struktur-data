import numpy as np

# akses array
arr = np.array([4, 3, 2, 1])
print(arr[3])

# perulangan tidak bersarang dari array
var = np.array([4, 3, 2, 1])
for x in var:
 print(x)

# perubahan isi array
var1 = np.array([4, 3, 2, 1])
print(var1[1])
var1[1] = 10;
print(var1[1])
