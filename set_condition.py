h = {1,9,12,7,14}
f = {6,9,8,10,5,11,12,13,15}
c = {2,4,9,3,5,13}

print(h|f|c)
print(h&f&c)
print(h - (f|c))
print(f^c) #symmetric difference