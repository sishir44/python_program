#Positional Argument: depends upon position of the paramenter
def pow_of(a,b):
    c=a**b
    print (c)
pow_of(5, 2) #25
pow_of(2, 5) #32
#pow_of(5) #error


#Default Argument(Optional)
#def pow_of(a,b=0,d,e): not possible
#def pow_of(a,d,e,f,b=0): possible
def pow_of(a,b=0):
    c=a**b
    print(c)
pow_of(2)


#Keyword argument:position doesn't matter
def pow_of(a,b):
    c=a**b
    print(c)    
pow_of(a=2,b=5)
pow_of(b=5,a=2)


#Varable length arguent(Arbitary)
'''def pizza_topping(*topping):
    print(topping)
pizza_topping("cheese")
pizza_topping("cheese","onion","olives","corn")'''

def pizza_topping(*topping, crust):
    print(topping)
    print(crust)
#pizza_topping("cheese","onion","olives","corn","thin")
pizza_topping("cheese","onion","olives","corn",crust="thin")


#Variable length keyword argument
def collect_student_data(**data):
    print(data)
collect_student_data(Name='sishir',age='23',dept='cse',Gender='Male')







































