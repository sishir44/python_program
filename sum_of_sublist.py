lst = input("Enter a list between []\n")
lst = eval(lst) #convert string to list

start = int(input("Enter the start index\n"))
stop = int(input("Enter the stop index\n"))

print("Sum =",sum(lst[start:stop+1]))