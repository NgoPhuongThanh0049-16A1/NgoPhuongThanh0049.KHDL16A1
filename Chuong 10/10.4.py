# Sử dụng hàm pow
import math
x = eval(input("Nhập số x: "))
n = eval(input("Nhập số n: "))
S = math.pow(math.pow(x,2)+x+1,n) + math.pow(math.pow(x,2)-x+1,n)
print("S =",S)