
from functools import reduce
n = input("Enter the numbers\n").split()
#print(n)
#print(type(n))
l = list(map(int,n))
#print(l)
res = reduce(lambda x,y:x+y,l)
#print(res)
avg = res/len(l)
print("{0:.3f}".format(avg))