n = int(input("Enter N : \n"))
res = []
for i in range(1,n+1):
    res.append((i,i**3))
print(res)

#using list Comprenshive
print([(i,i**3) for i in range(1,int(input("Enter N :"))+1) ])