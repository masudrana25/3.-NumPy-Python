import numpy as np  

np1 = np.array([1,2,3,4]) ; np2 = np.array([2,4,6,8]) 
np3 =np.array([[1,4],[3,5]]) ;  np4 =np.array([[2,8],[6,10]]) 
np5 = np.array([[345,43454],[335,535]])


#### Normal Reciprocal in one array ####

# Reciprocal of 1-D Array 
n_rec_1 = 1 / np1 ; # print(n_rec_1)  

# Reciprocal of 2-D Array 
n_rec_2 = 1 /np3 ; # print(n_rec_2)


#### Matrix Reciprocal in one array ####

# Reciprocal of 1-D Array 
m_rec_1 = np.reciprocal(np1) ; # print(m_rec_1)  

# Reciprocal of 2-D Array 
m_rec_2 = np.reciprocal(np5) ; # print(m_rec_2)



#### sum in one array ####
sum_of_np1 = np.sum(np1) ; # print(sum_of_np1) 
sum_of_np2 = np.sum(np2) ; # print(sum_of_np2)
sum_of_np3 = np.sum(np3) ; # print(sum_of_np3)


#### summation in multiple array ####

# sum the same position element and make a new array 
# 1-D Array + 1-D Array
sum_1 = np1 + np2 ; # print(sum_1) 
sum_1 = np.add(np1,np2) ; # print(sum_1) 

# 1-D Array + 2-D Array , not working
# sum_2 = np1 + np3 ; # print(sum_2) # don't work as array dimension is not the same

# 2-D Array + 2-D Array
# sum_3 = np3 + np4 ; # print(sum_3) 
sum_3 = np.add(np3,np4) ; # print(sum_3) 


#### subtraction in multiple array ####

# sub the same position element and make a new array 
# 1-D Array - 1-D Array
# sub_1 = np1 - np2 ; # print(sub_1) 
sub_1 = np.subtract(np1,np2) ; # print(sub_1)

# 1-D Array - 2-D Array , not working
# sub_2 = np1 + np3 ; # print(sub_2) # don't work as array dimension is not the same

# 2-D Array - 2-D Array
sub_3 = np3 - np4 ; # print(sub_3) 
sub_3 = np.subtract(np3,np4) ; # print(sub_3)


#### Multiplication in multiple array ####

# mul the same position element and make a new array 
# 1-D Array * 1-D Array
# mul_1 = np1 * np2 ; # print(mul_1) 
mul_1 = np.multiply(np1 , np2) ; # print(mul_1) 


# 1-D Array * 2-D Array , not working
# mul_2 = np1 * np3 ; # print(mul_2) # don't work as array dimension is not the same

# 2-D Array * 2-D Array
# mul_3 = np3 * np4 ; # print(mul_3) 
mul_3 = np.multiply(np3 , np4) ; # print(mul_3) 


#### Division in multiple array ####

# div the same position element and make a new array 
# 1-D Array / 1-D Array
# div_1 = np1 / np2 ; # print(div_1) 
div_1 = np.divide(np1 , np2) ; # print(div_1) 

# 1-D Array / 2-D Array , not working
# div_2 = np1 / np3 ; # print(div_2) # don't work as array dimension is not the same

# 2-D Array / 2-D Array
# div_3 = np3 / np4 ; # print(div_3) 
div_3 = np.divide(np3 , np4) ; # print(div_3) 


#### Reminder in multiple array ####

# rem the same position element and make a new array 
# 1-D Array % 1-D Array
rem_1 = np1 % np2 ; # print(rem_1) 
rem_1 = np.remainder(np1 , np2) ; # print(rem_1) 
rem_1 = np.mod(np1 , np2) ; # print(rem_1) 

# 1-D Array % 2-D Array , not working
# rem_2 = np1 % np3 ; # print(rem_2) # don't work as array dimension is not the same

# 2-D Array % 2-D Array
rem_3 = np3 % np4 ; # print(rem_3) 
rem_3 = np.remainder(np3 , np4) ; # print(rem_3) 
rem_3 = np.mod(np3 , np4) ; # print(rem_3) 



#### Power of multiple array ####

# 1-D Array => pow =>  1-D Array
# pow_1 = np1 * np2 ; # print(pow_1) # normal multiply
pow_1 = np.power(np1 , np2) ; # print(pow_1)  # matrix power

# 1-D Array => pow =>  2-D Array , not working
# pow_2 = np.power(np1,np3) ; # print(pow_2) # don't work as array dimension is not the same

# 2-D Array / 2-D Array
pow_3 = np.power(np3 , np4) ; # print(pow_3) 

