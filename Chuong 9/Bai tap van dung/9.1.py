# In ra giá trị theo dấu của 1 số 
import math
sign=lambda x: math.copysign(1,x)
print(sign(-8))
print(sign(8))