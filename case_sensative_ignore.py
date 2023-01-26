'''a to z = 97 to 122
A to Z = 65 to 90
to find ASCII value we use ord()
to find alphabet from ascii we use chr(ord')'''

c = "a"
print(ord(c))
print(ord(c)-32)
print(chr(ord(c)-32))


s = input("Enter a string\n")
s_upper = ""
for i in s:
    if ord(i)>=97 and ord(i) <= 122:
        s_upper += chr(ord(i)-32)
    else:
        s_upper += i
print(s)
print(s_upper)