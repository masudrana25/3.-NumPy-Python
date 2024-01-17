import numpy as np 

#### filter element from numpy array 
np1  = np.array([1,2,3,4,5,6,7,8,9])


## filter numpy array element by boolean value index
boolean_index = np.array([True, False, False,True,False,True,False,False,False])
filtered_element = np1[boolean_index] ; # print(filtered_element)

## filter with boolean index which is achieved by conditional comparison
# find even element
conditional_index = []
for element in np1 :
  if element % 2 ==0 : 
    # {{odd => element % 2 !=0}} , {{other condition => element >=5}}
    conditional_index.append(True)
  else :
    conditional_index.append(False)

conditional_element = np1[conditional_index] ; # print(conditional_element)

### shortcut filter
np1  = np.array([1,2,3,4,5,6,7,8,9])

even_filter_element_shortcut = np1[ np1 % 2 ==0] ; # print(even_filter_element_shortcut)

odd_filter_element_shortcut = np1[ np1 % 2 !=0] ; # print(odd_filter_element_shortcut)

conditional_filter_element_shortcut = np1[ np1 >=5] ; # print(conditional_filter_element_shortcut)

