'''Syntax:
    str.format(*args)  stored in tuple form'''

#1
name = input("Enter your name\n")
place = input("Enter your place\n")
s = "hello {},How is the weather in {}".format(name,place)
print(s)


#2
s = "{} {} {}".format(10,20,30)
print(s)

s1 = "{2} {0} {1}".format(10,20,30)
print(s1)