'''The NumPy searchsorted() function can be used to find the index value where the new elements should be inserted in the sorted array, and the order of an array be preserved. If the same elements are already present in a sorted array, then we can specify to insert the left or right of it'''
# kono akta element k kon index a rakha jai / achy

import numpy as np 

np1 = np.array([1,2,3,4,8,9,10,11]) ; np2 = np.array([ [1,2,3],[4,5,6], [7,8,9]]) 

# find the index of a element which belongs to the array
searchsorted_1 = np.searchsorted( np1, 3) ; print(searchsorted_1) 
searchsorted_1 = np.searchsorted( np1, 1) ;  print(searchsorted_1) 
searchsorted_1 = np.searchsorted( np1, 11) ; print(searchsorted_1) 

# find the index of a element which does not belongs to the array
searchsorted_1 = np.searchsorted( np1, 5) ; # print(searchsorted_1) 
searchsorted_1 = np.searchsorted( np1, 7) ;  print(searchsorted_1)
searchsorted_1 = np.searchsorted( np1, [5,6],side = 'left') ; # print(searchsorted_1) 
searchsorted_1 = np.searchsorted( np1, [5,6,7]) ; # print(searchsorted_1) 
