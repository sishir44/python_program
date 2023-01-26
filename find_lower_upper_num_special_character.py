s = input("Enter a string\n")
low_count,up_count,sp_count,num_count = 0,0,0,0

for i in s:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    elif i.isnumeric():
        num_count += 1
    else:
        sp_count += 1
        
print("Lower case =",low_count)
print("Upper case =",up_count)
print("Numeric case =",num_count)
print("Special case =",sp_count)