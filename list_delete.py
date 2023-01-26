lst = [10,20,30,40,50,60]
print(lst)
lst.remove(30) #delete one element
print(lst)

lst1 = [10,20,30,40,50,60]
print(30 in lst1) # membership operator
print(30 not in lst1)

lst2 = [10,20,30,40,50,60,30]
while(30 in lst2):
    lst2.remove(30)
print(lst2)

