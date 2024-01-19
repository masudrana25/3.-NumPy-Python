import numpy as np 

np1 = np.matrix([1,2,3,4]) ; np2 = np.matrix([2,4,6,8]) 
np3 =np.matrix([[1,4],[3,5]]) ;  np4 =np.matrix([[2,8],[6,10]]) 
np5 = np.matrix([[345,43454],[335,535]])

# print(type(np1)) # <class 'numpy.matrix'>

#### sum in one matrix ####
sum_of_np1 = np.sum(np1) ; # print(sum_of_np1) 
sum_of_np1 = np.sum(np2) ; # print(sum_of_np1)
sum_of_np1 = np.sum(np3) ; # print(sum_of_np1)
sum_of_np1 = np.sum(np4) ; # print(sum_of_np1)
sum_of_np1 = np.sum(np5) ; # print(sum_of_np1)


#### summation in multiple matrix ####

# sum the same position element and make a new array 
# 1-D matrix + 1-D matrix
sum_1 = np1 + np2 ; # print(sum_1) 
sum_1 = np.add(np1,np2) ; # print(sum_1) 

# 1-D matrix + 2-D matrix , not working
# sum_2 = np1 + np3 ; # print(sum_2) # don't work as matrix dimension is not the same

# 2-D matrix + 2-D matrix
sum_3 = np3 + np4 ; # print(sum_3) 
sum_3 = np.add(np3,np4) ; # print(sum_3) 


#### subtraction in multiple matrix ####

# sub the same position element and make a new matrix 
# 1-D matrix - 1-D matrix
sub_1 = np1 - np2 ; # print(sub_1) 
sub_1 = np.subtract(np1,np2) ; # print(sub_1)

# 1-D matrix - 2-D matrix , not working
# sub_2 = np1 + np3 ; # print(sub_2) # don't work as matrix dimension is not the same

# 2-D matrix - 2-D matrix
sub_3 = np3 - np4 ; # print(sub_3) 
sub_3 = np.subtract(np3,np4) ; # print(sub_3)


#### transpose matrix ####
np2 = np.matrix([2,4,6,8]) ; np3 =np.matrix([[1,4],[3,5]])

transpose_1 = np.transpose(np2) ; # print(transpose_1)
transpose_1 = np.transpose(np3) ; # print(transpose_1)
transpose_1 = np2.T ; # print(transpose_1)
transpose_1 = np3.T ; # print(transpose_1)


#### swapaxes matrix ####
np2 = np.matrix([2,4,6,8]) ; np3 =np.matrix([[1,4],[3,5]])

swapaxes_1 = np.swapaxes(np2,0,1) ; # print(swapaxes_1)
swapaxes_1 = np.swapaxes(np3,0,1) ; # print(swapaxes_1)
swapaxes_1 = np.swapaxes(np3,1,0) ; # print(swapaxes_1)


#### inverse matrix ####
np2 = np.matrix([2,4,6,8]) ; np3 =np.matrix([[1,4],[3,5]]) ; np5 = np.matrix([[345,43454],[335,535]])

# 1-d matrix er inverse hoina
# inverse_1 = np.linalg.inv(np2) ; #  print(inverse_1)

inverse_1 = np.linalg.inv(np3) ; # print(inverse_1)
inverse_1 = np.linalg.inv(np5) ; # print(inverse_1)


#### matrix power ####
# A^2 = A * A ; A^0 = I ;
np3 =np.matrix([[1,4],[3,5]]) ; np5 = np.matrix([[345,43454],[335,535]])

power_1 = np.linalg.matrix_power(np3,2) ; # print(power_1)


#### matrix determinant ####
np3 =np.matrix([[1,4],[3,5]]) ; np5 = np.matrix([[345,43454],[335,535]])

determinant_1 = np.linalg.det(np3) ; print(determinant_1)
determinant_1 = np.linalg.det(np5) ; print(determinant_1)

