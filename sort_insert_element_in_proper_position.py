lst = eval(input("enter a sorted list between []\n"))
n = int(input("Enter the value to be inserted\n"))
print(lst)

for i in range(len(lst)):
    if n<lst[i]:
        lst.insert(i,n)
        break
print(lst)