import numpy as np 

np1 = np.array([1,2,3,4,5,7,1,3,9,2]) 


# unique array return => repeated element will be remove form array and new array will be returned
unique_1 = np.unique(np1) ; # print(unique_1) 


# unique array return with repeated element index, count 
# np.unique( array_name, return_index, return_count)
# return array = [ [unique array], [repeated element index], [repeated element count]]
unique_2 = np.unique(np1, return_index=True, return_counts=True)
print(unique_2) ; print(unique_2[0]) ; print(unique_2[1]) ; print(unique_2[2])

