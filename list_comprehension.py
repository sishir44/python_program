#list comprehension
#[Whatiwant Fromwhichloop Onwhatcondition]

lst = [2,5,7,8,10]
print([i**2 for i in lst])
print([i**2 for i in lst if i%2==0 ])
print([i**2 for i in lst if i%2!=0 ])