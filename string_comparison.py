#compare two value
s1="Python"
s2="Java"
if(s1 == s2):
    print("String are equal")
else:
    print("String are not equal")
     
   
#compare address of two value    
s1="Python"
s2="Python"
if id(s1) == id(s2):
#if s1 is s2: -> denotes references 
    print("Reference are equal")
else:
    print("Reference are not equal")
    
    
#case sensative
s1="python"
s2="PYTHON"
if s1 == s2:
    print("string values are equal")
else:
    print("string values are not equal")