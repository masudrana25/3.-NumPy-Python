import numpy as np 

### np.insert(array_name, position_where_element_will_be_inserted, inserted_elements) ###

# 1-D Array
np1 = np.array([1,2,3,4])
insert_1 = np.insert(np1,2,7) ; # print(insert_1)
insert_1 = np.insert(np1,2,7.55) ; # print(insert_1) # not take the decimal point

insert_2 = np.insert(np1,2,[7,8,5]) ; # print(insert_2)

insert_3 = np.insert(np1,(2,4),7) ; # print(insert_3)
insert_3 = np.insert(np1,(2,4),(7,9)) ; # print(insert_3)
insert_3 = np.insert(np1,(2,4),[7,9]) ; # print(insert_3)


# 2-D Array
np2 = np.array([ [1,2],[3,4]]) ; # print(np2)

insert_4 = np.insert(np2,0,7, axis = 0 ) ; # print(insert_4) 
insert_4 = np.insert(np2,0,7, axis = 1 ) ; # print(insert_4) 

insert_4 = np.insert(np2,0,[7,9], axis = 0 ) ; # print(insert_4) 
insert_4 = np.insert(np2,0,[7,9], axis = 1 ) ; # print(insert_4) 
insert_4 = np.insert(np2,2,[7,9], axis = 0 ) ; # print(insert_4) 
insert_4 = np.insert(np2,2,[7,9], axis = 1 ) ; # print(insert_4) 

np3 = np.array([ [1,2,3],[4,5,6]]) ; # print(np3)

insert_5 = np.insert(np3,0,[77,88,99], axis = 0 ) ; # print(insert_5) 
insert_5 = np.insert(np3,0,[77,99], axis = 1 ) ; # print(insert_5) 

