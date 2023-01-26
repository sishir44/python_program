
# Every character is repeat only once

s = "The Big Dwarf only Jumps!".upper()

l = []

for i in s:
    if ord(i) >=65 and ord(i) <=90:
        l.append(i)
        
c = set(l)
if len(l) == len(c):
    print(s,"is a Heterogram")
else:
    print(s,"is not a heterogarm")