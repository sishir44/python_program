'''Syntax:
    for var in iterable:
        //body pof loop
        where for-keyword, var is variable, in is operator,
        iterable may be list,tuple,set,dict and so on'''
        
lst=[10,20,30,40,50]
for i in lst:
    print(i)
    
'''for i in [1,2,3,4,5]:
    print('python')'''
    
for i in range(5): #start from 0 to 4 ie 0,1,2,3,4
    print("Python")
    
print(list(range(2,10)))
print(list(range(2,10,2)))
print(set(range(2,10)))
print(tuple(range(2,10)))


balance = 15500
min_balance = 500
print("Before transaction : ", balance)
for i in range(5):
    balance = balance-1000
print("After transaction : ", balance)







