lst1 = [10,20,30,40]
lst2 = [35,20,10,15]

for i in lst2:
    if i not in lst1:
        lst1.append(i)
print(lst1)