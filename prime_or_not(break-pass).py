n = int(input("Enter a number\n"))
for i in range(2,n+1):
    if(n%i == 0):
        break#pass
if(i == n):
    print(n, "is prime")
else:
    print(n, "is not prime")