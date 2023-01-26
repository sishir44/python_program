#ADDING LIST
lst = [10,20,30,40,50]
print(lst)

lst.append(60)# add single element only
print(lst)

#lst.append([70,80,90])
#print(lst)

#lst = lst + [70,80,90] #add multiple 
#print(lst)

lst.extend([70,80,90]) #add multiple 
print(lst)

lst.insert(2, 99)
print(lst)