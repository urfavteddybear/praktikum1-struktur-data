data_siswa=[[132,133,134],[1,1,3]]
print(data_siswa[1])

var = [[132, 133, 134],[1, 3], ["Dono", "Kasino", "Indro"]]
print(var[2][1])

# perulangan list
var1 = [[132,133,134],[1,1,3]]
for x in var1:
 print(x)

var2 = [[132, 133, 134],[1, 3], ["Dono", "Kasino", "Indro"]]
for x in var2:
 for y in x:
  print(y)

# perubahan isi list
var3 = [[132, 133, 134],[1, 3], ["Dono", "Kasino", "Indro"]]
print(var3[2][1])
var3[2][1] = "Budi"
print(var3[2][1])
