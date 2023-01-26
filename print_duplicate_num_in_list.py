lst = list(map(int, input().split() ))
s = set(lst)
print(len(lst) - len(s))
