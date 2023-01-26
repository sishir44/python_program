s = {5,4,9,8,7,2}
print({i**2 for i in s})
print({i**2 for i in s if i%2==0})
print({i**2 for i in s if i%2})

print({i**2 if i%2==0 else i+i for i in s})
