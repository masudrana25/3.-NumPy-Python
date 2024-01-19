import numpy as np

#### Element-wise Multiplication #### 
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2 ; # print(result)


#### Matrix Multiplication (Dot Product) #### 
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
result = array1 @ array2 ; # print(result)


#### Inner Product for 1-d #### 
# same position er element gula k gun korey sum korbey
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
inner_product = np.inner(array1, array2) ; # print(inner_product)


#### Outer Product #### 
# first array er akta element diye 2nd array er sob gula element k gun kora hby and akta row borabor sei gun er value gula rakha hby . avabey 1st array er sob gula element diye 2nd array er sob gula element k gun korty hby.

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([[1, 2], [3, 4]])
array4 = np.array([[5, 6], [7, 8]])
outer_product = np.outer(array1, array2) ; # print(outer_product)
outer_product = np.outer(array1, array3) ; # print(outer_product)
outer_product = np.outer(array3, array4) ; # print(outer_product)


#### Scalar Multiplication #### 
scalar = 2
array = np.array([1, 2, 3])
array3 = np.array([[5, 6], [7, 8]])
scaled_array = scalar * array ; # print(scaled_array)
scaled_array = scalar * array3 ; # print(scaled_array)


#### Element-wise Power #### 
array = np.array([2, 3, 4]) ; array3 = np.array([[5, 6], [7, 8]])
exponent = 2
result_power = np.power(array, exponent) ; # print(result_power)
result_power = np.power(array3, exponent) ; # print(result_power)

