lst1 = ['A','app','da','kee','t','doc','a']
lst2 = ['n','le','y','ps','he','tor','way']

print(' '.join([i+j for i,j in zip(lst1,lst2)]))


s = input("Enter a string\n")
lst = s.split()
print(' '.join([lst[i].lower() if len(lst[i]) > 5 else lst[i].upper() for i in range(len(lst))]))
