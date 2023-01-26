
#Traditional Approach

lst = [3,6,5,4,2]
res = []
for i in lst:
    if i%2 == 0:
        res.append(i*i)
        
    else:
        res.append(i+i)
        
print(lst)
print(res)
    

#using list comprehensive
lst = [4,6,5,4,2]
res = [i*i if i%2 == 0 else i+i for i in lst]
print(lst)
print(res)
