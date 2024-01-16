import numpy as np

# shape = (row, column)

#### create a 1-D Numpy Array and find shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
length_of_np1 = np1.shape; # print(length_of_np1)

#### create a 2-D Numpy Array and find shape
np2 = np.array(
  [
    [1,2,3,4,5,6,7,8,9],
    [11,12,13,14,15,16,17,18,19]
  ]
)
length_of_np2 = np2.shape ; # print(length_of_np2)

#### 1-D reshape to 2-D
np3 = np1.reshape(3,4) ; # print(np3) ; print(np3.shape)

#### 1-D reshape to 3-D
np4 = np1.reshape(2,3,2) ; # print(np4) ; print(np4.shape)

#### 2-D reshape to 1-D
np5 = np3.reshape(-1) ; # print(np5) ; print(np5.shape)

#### 3-D reshape to 1-D
np6 = np4.reshape(-1) ; # print(np6) ; print(np6.shape)


