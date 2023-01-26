#fun without input, without return value
def mul():
    a=10
    b=20
    c=a*b
    print(c)
mul() 


#fun with input, without return value
def mul(x,y):
    c=x*y
    print(c)
mul(10,20)


#fun without input, with return value
def mul():
    a=10
    b=20
    c=a*b
    return c
res=mul()
print(res)


#fun with input, with return value
def mul(x,y):
    c=x*y
    return c
res=mul(10,20)
print(res)




























