#all() it return only true value if all are true
#any() it return only true value if any one is true

lst = [-10,-20,-30,-40,-50,60]

print(all([i>0 for i in lst]))
print(any([i>0 for i in lst]))