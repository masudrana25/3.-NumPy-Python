import numpy as np

#### Standard Matrix Multiplication (Dot Product) #### 
# This is the standard matrix multiplication where the dot product of rows and columns is calculated.
matrix1 = np.matrix([[1, 2], [3, 4]]) 
matrix2 = np.matrix([[5, 6], [7, 8]]) 
result_standard = matrix1 * matrix2 ; # print(result_standard)
result_standard = np.dot(matrix1, matrix2) ; # print(result_standard)


