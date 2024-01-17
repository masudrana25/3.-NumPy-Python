import numpy as np 

np1 = np.array([1,2,3,4]) ; np2 = np.array([2,4,6,8]) 
np3 =np.array([[1,4],[3,5]]) ;  np4 =np.array([[2,8],[6,10]]) 
np5 =np.array([[1,4,6],[3,5,7]]) ;  np6 =np.array([[2,8,9],[6,10,3]])


# 1-D stack
# column borabor join korby array duita k
stack_1 = np.stack((np1,np2)) ; # print(stack_1)

# column borabor join korby array duita k with axis=1 
stack_1 = np.stack((np1,np2), axis =1) ; # print(stack_1)

# 2-D stack 
stack_2 = np.stack((np3,np4)) ; # print(stack_2)
stack_2 = np.stack((np3,np4), axis = 2) ; # print(stack_2)

stack_2 = np.stack((np5,np6)) ; # print(stack_2)
stack_2 = np.stack((np5,np6), axis = 2) ; # print(stack_2)




