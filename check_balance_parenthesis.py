s = input("Enter an expression with brackets\n")
lst = []

for i in s:
    
    if i == '[' or i == '(' or i == '{':
        lst.append(i)
        
    elif i == ']' and lst[-1] == '[':
        lst.pop()
        
    elif i == ')' and lst[-1] == '(':
        lst.pop()
        
        
    elif i == '}' and lst[-1] == '{':
        lst.pop()
        
    else:
        break
if len(lst) == 0:
    print(s,"Expression is balanced")
    
else:
    print(s,"Expression is not balanced")
    