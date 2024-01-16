import numpy as np 

######### view vs copy ######### 

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

######## create a view
''' view = copy the view array. the original and view array are inter-connected. if original array is changed, then the view array will be also changed. Similarly if the view array is changed, then the original array will be also changed.'''

# np2 = np1.view()

# print(f" Original np1 Array : {np1}") ; print(f" Original np2 Array : {np2}")

# np1[0] = 44
# np2[0] = 44

# print(f" changed np1 Array : {np1}") ; print(f" Original np2 Array : {np2}")




############ create a copy
''' copy = copy the array. the original and copy array are not inter-connected. if original array is changed, then the copy array will not be also changed. Similarly if the copy array is changed, then the original array will not be also changed. '''

# np3 = np1.copy()

# print(f" Original np1 Array : {np1}") ; print(f" Original np3 Array : {np3}")

# np1[0] = 44
# np3[0] = 44

# print(f" after changed np1 Array : {np1}") ; print(f" after changed np3 Array : {np3}")