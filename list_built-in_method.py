lst = [15,55,30,43,38]
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))

for i in range(len(lst)):
    print(i, lst[i])
  #or   
for i,j in enumerate(lst):
    print(i,j)
  

lst =sorted(lst,reverse = True)
print(lst)

lst.sort(reverse=True)
print(lst)

lst.reverse()
print(lst)
