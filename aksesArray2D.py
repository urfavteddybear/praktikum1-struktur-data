import numpy as np

# akses array 2d
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,1])

# akses array 2d perulangan bersarang
var1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
for x in var1:
 for y in x:
  print(y)
  
# perubahan isi array dalam array2d  
var2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(var2[1,1])
var2[1][1] = 99;
print(var2[1,1])
