'''while loop => infinite loop
syntax:
    initialize;
    while(condition):
        print()
        increment/decrement'''

lst = [10,20,30,40,50]
i=0 # 0 is an index
while(i<5):
    print(lst[i])
    i = i+1 # if we dont use incr\decr then it goes infinite


balance = 1500
min_balance = 500
print("Before transaction : ", balance)
while(min_balance < balance):
    balance = balance-1000
print("After transaction : ", balance)