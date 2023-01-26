#function which calls itself called recursive function
n = int(input("Enter a numner\n"))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))