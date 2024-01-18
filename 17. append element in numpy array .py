import numpy as np 

np1 = np.array([1,2,3,4,5]) 

# last a element add
append_1 = np.append(np1,2) ; # print(append_1)
append_1 = np.append(np1,6.77) ; # print(append_1)
append_1 = np.append(np1,[7,8,9,10,11]) ; # print(append_1)

# 2-D
np2 = np.array([
  [1,2,3],
  [4,5,6]
])

# last a element add
append_2 = np.append(np2, [[11,12,13]], axis = 0) ; # print(append_2)


