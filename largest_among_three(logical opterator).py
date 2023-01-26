#Logical operator => and, or, not, all are small letter

a=int(input("Enter a first number : "))
b=int(input("Enter a second number : "))
c=int(input("Enter a third number : "))
if(a>b and a>c):
    print("a is largest")
elif(b>c):
    print("b is largest")
else:
    print("c is largest")