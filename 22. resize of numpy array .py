import numpy as np 

np1 = np.array([1,2,3,4,5,6]) 

# resize the array with new row and column 
resize_1 = np.resize(np1,(3,2)) ; # print(resize_1)
resize_1 = np.resize(np1,(2,3)) ; # print(resize_1)

np2 = np.array([[1,2],[3,4],[5,6]])

resize_2 = np.resize(np2,(1,6)) ; print(resize_2)
resize_2 = np.resize(np2,(2,3)) ; print(resize_2)
