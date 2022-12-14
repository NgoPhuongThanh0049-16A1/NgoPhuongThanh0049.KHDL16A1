# Xây dựng phương thức tinh_S(n,x)
import math
x = int(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = lambda x, n: math.pow(math.pow (x,2)+1,n)
print("S=(x^2+1)^n","=",S(x,n))
