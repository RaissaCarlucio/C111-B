# Guilherme Muniz de Oliveira Reis
# Engenharia de Software - Integral
# P7        Mat - 127

import numpy as np

arr = np.loadtxt('C:/Users/usuario/Desktop/C111-B/Prova 1/brands.csv',
                 delimiter=';', dtype=str, encoding='utf-8')
arr = np.array(arr[1:])

# Ex1
microsoft = np.where(arr[::, 0] == 'Microsoft')
microsoft = arr[microsoft]
#print(microsoft)
microsoft = np.array(microsoft[0])
#print(microsoft)

#print(float(microsoft[9])-float(microsoft[10]))

# # Ex2
# brand = np.array(arr[::, 0], dtype=str)
# #brand = brand[str(brand)[0] == 'A']
# #brand = np.where(str(brand[::][0]) == 'A')
# #brand = brand[np.where(brand[0]=='A')]
# brand = np.sort(brand)
# #print(brand)

# #Ex3
usa = np.where(arr[::, 3] == 'United States')
usa = arr[usa]
print(usa)
usa = (usa.size/arr.size)*100

print("%.2f" % (usa) + " %")

# #Ex4
# sliced = arr[1::, :3]
# sliced_f = np.array(arr[::, 2], dtype= np.int32)
# sliced_f = np.where(sliced_f >= 2000)
# sliced = arr[sliced_f]
# #print(sliced)

# #Ex5
founded = np.unique(arr[::, 2], return_counts=True)
founded = np.array(founded)
founded_max = np.array(founded[1], dtype=np.int32)  #Slicing para obter somente as quantidades
founded_max = str(founded_max.max())
founded_max = np.where(founded[1, ::] == founded_max)
founded_max = founded[0, founded_max]
print(founded_max)
