#In shallow copy, only the outer list is copied
#shallow copy
lst1 = [[10,20],[30,40]]
lst2 = list(lst1) #it creates shallow copy
lst2 = lst1[:]
print(lst1)
print(lst2)
print(lst1 is lst2)

lst1.append([50,60])
print(lst1)
print(lst2)

lst1[1][0] = 300
print(lst1)
print(lst2)
