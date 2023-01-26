lst1 = [2,4,5]
lst2 = [5,4,2,1]
res = []

for i in lst1:
    for j in lst2:
        if i != j:
            res.append((i,j))
print(res)

#using list comprehshive

lst1 = [2,4,5]
lst2 = [5,4,2,1]
res = [(i,j) for i in lst1 for j in lst2 if i!=j]
print(res)
