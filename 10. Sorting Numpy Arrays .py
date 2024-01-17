import numpy as np 

# sorting new array return a copy of sorting the original array . if we change them, it does not influence each other.

#### sorting numpy array (contain number) elements
np1 = np.array([6,5,8,3,9,1,0])
sorted_np1 = np.sort(np1) ; # print(sorted_np1)

#### sorting numpy array (contain string) elements
np2 = np.array(['Masud','Sabbir','Abdul Alim','Jabbar','Sanjida','Hasib','Sajidul'])
sorted_np2 = np.sort(np2) ; # print(sorted_np2)

#### sorting numpy array (contain booleans) elements
np3 = np.array([True , False , False , True , True , True, False ])
sorted_np3 = np.sort(np3) ; # print(sorted_np3)

#### sorting numpy array ( 2-D) elements
np4 = np.array(
  [
    [6,5,8,3,9,1,0],
    [-3,-6,4,7,8,99,0]
  ]
)
sorted_np4 = np.sort(np4) ; # print(sorted_np4)



