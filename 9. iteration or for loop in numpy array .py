import numpy as np

####### normal iteration process using for loop


#### 1-D array

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# for x in np1 : 
#   print(x)


#### 2-D array

np2 = np.array([ [1,2,3,4,5], [6,7,8,9,10] ])
# for x in np2 : 
#   # print(x) # printed the rows of 2-D array
#   for y in x :
#     print(y)


#### 3-D array

np3 = np.array(
  [
    [ [1,2,3,4] , [5,6,7,8] ],
    [ [9,10,11,12], [13,14,15,16] ]
  ]
)
# for x in np3 : 
#   # print(x) # printed the main rows of 3-D array
#   for y in x :
#     # print(y) # printed the sub rows of 3-D array
#     for z in y :
#       print(z) # printed the sub rows of 3-D array element


####### numpy iteration process

for x in np.nditer(np1) : 
  print(x) # print the sub rows of 1-D array element

for x in np.nditer(np2) : 
  print(x) # print the sub rows of 2-D array element

for x in np.nditer(np3) : 
  print(x) # print the sub rows of 3-D array element


