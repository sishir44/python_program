
#ONE way
s = "Nepal is my country"
vow_s = "aeiouAEIOU"
res = []
for i in s:
    if i in vow_s:
        res.append(i)
print(len(res))

#ANOTHER WAY
s = "Nepal is my country"
vow_s = "aeiouAEIOU"
print(len([i for i in s if i in vow_s]))


print(len([i for i in input() if i in "aeiouAEIOU"]))