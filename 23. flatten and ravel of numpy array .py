import numpy as np 

np2 = np.array([[1,2],[3,4],[5,6]])

### flatten=> flat or horizontally sob gula element k bosabey and new array create korbey
# order = "C" => default order => row wise flat korbey
# order = "F" => column wise flat korbey

flatten_1 = np2.flatten() ; # print(flatten_1)
flatten_1 = np2.flatten(order = "C") ; # print(flatten_1)
flatten_1 = np2.flatten(order = "F") ; # print(flatten_1)


### np.ravel => flat or horizontally sob gula element k bosabey and new array create korbey

revel_1 = np.ravel(np2, order="C") ; # print(revel_1)
revel_1 = np.ravel(np2, order="F") ; # print(revel_1)

