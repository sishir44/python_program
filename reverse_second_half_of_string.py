'''reverse second half of string
we use floor operator(//)
floor is used to remove decimal part'''
#eg 3.5 then we considered only 3
s = input("Enter a string\n")
print(s[:len(s)//2:] +
s[len(s)-1 : (len(s)//2)-1 : -1])
