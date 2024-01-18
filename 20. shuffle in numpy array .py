# অদলবদল => Modify a sequence in-place by shuffling its contents. This function only shuffles the array along the first axis of a multi-dimensional array.

import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9]) ; np2 = np.array([3,5,7,2,8,9,1]) 
np3 = np.array([1,4,8,2,3,7,9,5,4,7])

np.random.shuffle(np1) ; print(np1)
np.random.shuffle(np2) ; print(np2)
np.random.shuffle(np3) ; print(np3)

# original array er moddhy change korbey

# shuffle_1 = np.random.shuffle(np1) ; print(shuffle_1)
# shuffle_1 is none => nothing will be same in new array. it just change the original array and same the original array as changed array



