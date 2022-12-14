x = eval(input("Nhập x: "))
n = eval(input("Nhập n: "))
import math
s = lambda x, n: math.pow (math.pow(x,2)+1,n)
print("s= ",s(x,n))