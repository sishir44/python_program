'''syntax:
    string_name[start:stop:step]'''
  
    
s = "Guido Van Rossum"
print(s)
print(s[::])
print(s[0:5:1])
print(s[0:9:2])
print(s[15:9:-1])
print(s[-1:-7:-1])

#Reverse a string
print(s[::-1])