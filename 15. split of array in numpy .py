import numpy as np 

# split break one array into multiple arrays
# the resultant array is a "class list"

#### 1-D Array Split #### 
np1 = np.array([1,2,3,4,5,6,7,8,9,10])

### np.split(array_name,number_of_split_array)
'''numpy.split: Requires that the array can be equally divided by the specified number of splits. It divides the array into equal parts along the specified axis.'''

split_1 = np.split(np1,2) ; # print(split_1) ; # print(type(split_1)) ; # print(split_1[0]) ; # print(split_1[1])
split_2 = np.split(np1,5) ; # print(split_2) ; # print(split_2[0]) ; # print(split_2[4])

### np.array_split(array_name,number_of_split_array)
'''numpy.array_split: Allows for an uneven division of the array. It can handle cases where the array cannot be evenly divided by the number of splits.'''

split_3 = np.array_split(np1,3) ; # print(split_3) ; # print(type(split_3)) ; # print(split_3[0]) ; # print(split_3[1])
split_4 = np.array_split(np1,4) ; # print(split_4) ; # print(split_4[0]) ; # print(split_4[4])


#### 2-D Array Split #### 
np2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

### np.split
split_5 = np.split(np2,3) ; # print(split_5) ; # print(type(split_5)) ; # print(split_5[0]) ; # print(split_5[1])

### np.array_split
split_6 = np.array_split(np2,3) ; # print(split_6) ; # print(split_6[0]) ; # print(split_6[2])





