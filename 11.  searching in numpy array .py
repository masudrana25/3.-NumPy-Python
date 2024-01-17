import numpy as np 

#### searching elements in a numpy array ####
np1 = np.array([1,2,3,4,5,6,7,8,9,3,4,5,3])
 
## searching_element_index_with_datatype is a array which contain searching elements index and datatype 
searching_element_index_with_datatype = np.where( np1 == 3) 
# print(searching_element_index_with_datatype) 

## searching_element_index is a array that contain only the searching elements index
searching_element_index = searching_element_index_with_datatype[0]
# print(searching_element_index) 

## searching_element is a array that contain only the searching elements
searching_element = np1[searching_element_index]
# print(searching_element) 


## search in 2-D array
np2 = np.array([[8,9,3,4,5,3],[1,2,3,4,5,6]])
# print(np2)
searching_element_index_2d = np.where(np2 == 3)[0] # it gives the row index only
# print(searching_element_index_2d)

np3 = np.array([1,2,3,4,5,6,7,8,9])

## Return the even element of the array
even_element_index = np.where( np3 % 2 ==0) 
even_element = np3[even_element_index] ; # print(even_element)

## Return the odd element of the array
odd_element_index = np.where( np3 % 2 !=0) 
odd_element = np3[odd_element_index] ; # print(odd_element)

## Return element with a condition from the array
conditional_element_index = np.where( np3 >= 5) 
conditional_element = np3[conditional_element_index] ; # print(conditional_element)