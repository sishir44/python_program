x=99   #global variable
def fun():
    y=999   #local variable
    print(y)
    print(x)
fun()
print(x+x)# possible
#print(y)  not possible NameError


#local variable name = global var name
x=99
def fun():
    x=999
    print(x) #preference is given to local
fun()
print(x)


#we can make local variable as global using global keyword
x=99
def fun():
    global x
    x=999
    print(x) #999 but its global
fun()
print(x) #999 but its global