# 2.Presentation = f-(fixed point notation), e-(exponent notation)

import math
print(math.pi)

s = "{0:.4f}".format(math.pi)
#s = "{0:010.4f}".format(math.pi)
print(s)

ew = 76590000000000000000000000000
s = "{0:.3e}".format(ew)
print(s)

#s1 = "{} {} {}".format([10,20,30])
s1 = "{} {} {}".format(*[10,20,30])
print(s1)