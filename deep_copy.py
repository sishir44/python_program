#In deep copy, both the outer and inner list was copied
#deep Copy to avoid shallow copy

import copy
lst1 = [[10,20],[30,40]]
lst2 = copy.deepcopy(lst1) #it creates deep copy
print(lst1)
print(lst2)
print(lst1 is lst2)

lst1.append([50,60])
print(lst1)
print(lst2)

lst1[1][0] = 300
print(lst1)
print(lst2)