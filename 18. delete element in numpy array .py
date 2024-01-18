import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9]) ; np2 = np.array([ [1,2,3], [4,5,6] ]) 

# np.delete( array_name, deleted_element_index )
delete_1 = np.delete( np1, [2] ) ; print(delete_1)
delete_1 = np.delete( np1, [2,3,4,5] ) ; print(delete_1)



