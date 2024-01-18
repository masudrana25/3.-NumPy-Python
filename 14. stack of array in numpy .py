'''
The numpy stack() function is used to combine a series of arrays along a new axis. The numPy concatenate() function is also used to combine two or more arrays, but by using numPy stack(), we can combine arrays along a new axis.
'''

import numpy as np 

np1 = np.array([1,2,3,4]) ; np2 = np.array([2,4,6,8]) ;np2_2 = np.array([5,6,7,8])
np3 =np.array([[1,4],[3,5]]) ;  np4 =np.array([[2,8],[6,10]]) 
np5 =np.array([[1,4,6],[3,5,7]]) ;  np6 =np.array([[2,8,9],[6,10,3]])


#### 1-D stack

### vstack 
# => vertically join korbey array gula k 
# => column borabor join korbey 
# => akta column a sob gula array k rekhey new array create korby
# => 1st array ta k first row a rakhbey, 2nd array k 2nd row ty, 3rd array k 3rd row ty rakhbey. avabey akta new array form korbey

vstack_1 = np.vstack((np1,np2)) ; # print(vstack_1)
vstack_2 = np.vstack((np1,np2,np2_2)) ; # print(vstack_2)



### hstack 
# => horizontally join korbey array gula k
# => row borabor element gula k join korbey
# => sob gula array er element gula k niye, horizontally element gula k diye akta new array create korby

hstack_1 = np.hstack((np1,np2)) ; # print(hstack_1)
hstack_2 = np.hstack((np1,np2,np2_2)) ; # print(hstack_2)


## dstack 
# => height borabor join korbey array gula k
# => 1st array er sob element 1st column borabor boseby, 2nd array er sob element 2nd column borbabor boseby, 3rd array er sob element 3rd column bosbey. Then joita array join korbo, toita korey row borabor element niye akta row hobey. Then 2-D akta new array create korby

dstack_1 = np.dstack((np1,np2)) ; # print(dstack_1)
dstack_2 = np.dstack((np1,np2,np2_2)) ; # print(dstack_2)
# same with axis value
dstack_1 = np.stack((np1,np2), axis = 1) ; # print(dstack_1)
dstack_2 = np.stack((np1,np2,np2_2), axis = 1) ; # print(dstack_2)


#### 2-D stack 
# bujini
stack_2 = np.stack((np3,np4)) ; # print(stack_2)
stack_2 = np.stack((np3,np4), axis = 2) ; # print(stack_2)

stack_2 = np.stack((np5,np6)) ; # print(stack_2)
stack_2 = np.stack((np5,np6), axis = 2) ; # print(stack_2)




