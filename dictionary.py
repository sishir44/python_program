d = {1:'C',2:'Java',3:'Python'}
print(d)
d[4] = 'C++'
print(d)

d.update({5:'C#',6:'JS'})
print(d)

d.update(seven='Angular',eight='PHP')
print(d)

d.pop(3)
print(d)

d.popitem()
print(d)

del d[4]
print(d)