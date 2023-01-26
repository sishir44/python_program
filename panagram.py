#check if the sentence has all 24 alphabet or not
# The quick brown fox jumps over a lazy dog

s = "The Quick Brown Fox jumps over a Lazy Dog!"
s = s.upper()
c = set()


for i in s:
    if ord(i) >= 65 and ord(i) <=90:
        c.add(i)
if len(c) == 26:
    print(s,'is a pangram')
else:
    print(s,'not a pangram')




# Using Comprehensive
    
if len({i for i in s if ord(i)>=65 and ord(i) <= 90}) == 26:
    print(s,'is a pangram')
else:
    print(s,'not a pangram')

