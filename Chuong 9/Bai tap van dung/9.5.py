# Xây dựng chương trình tính A(x,n)
import math
x = int(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = float (((x*x+x+1)**n)+ ((x*x-x+1)**n))
print("S=(x^2+x+1)^n + (x^2-x+1)^n","=",S)


