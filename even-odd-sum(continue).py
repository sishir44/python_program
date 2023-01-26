even_sum, odd_sum = 0,0
n = int(input("Enter a value n \n"))
for i in range(1, n+1):
    if(n%2 == 0):
        even_sum += i
        continue
    odd_sum += i
print("sum of all even number : ",(even_sum))
print("sum of all odd number : ",(odd_sum))