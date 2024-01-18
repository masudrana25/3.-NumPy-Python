import numpy as np 

np1 = np.array([1,2,3,4]) ; np2 = np.array([2,4,6,8]) 
np3 =np.array([[1,4],[3,5]]) ;  np4 =np.array([[2,8],[6,10]]) 
np5 = np.array([[345,43454],[335,535]])

# join need double (()) brackets around

# 1-D join => axis = 0 => in x direction
join_1 = np.concatenate((np1,np2)) ; # print(join_1)


# 2-D join 
# axis = 0 => in y direction
# axis = 1 => in x direction
join_2 = np.concatenate((np3,np4),axis = 0) ;  print(join_2)
join_3 = np.concatenate((np3,np4),axis = 1) ;  print(join_3)


# 1-D with 2-D join
# join_3 = np.concatenate((np1,np3)) ; # print(join_3) # not possible



