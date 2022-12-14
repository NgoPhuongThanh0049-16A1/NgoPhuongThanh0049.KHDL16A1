# Sử dụng biểu thức lambda để tính 
a = eval(input("Nhập chiều dài hình chữ nhật: "))
b = eval(input("Nhập chiều rộng hình chữ nhật: "))
r = eval(input("Nhập bán kính hình tròn: "))
import math
# Diện tích, chu vi hình tròn
math.pi
S1 = lambda r : (r**2)*math.pi
P1 = lambda r : (2*r)*math.pi
print("S1 = ",S1(r))
print("P1 = ",P1(r))
# Diện tích, chu vi hình chữ nhật 
P2 = lambda a, b: ((a+b)*2)
S2 = lambda a, b: (a*b)
print("P2 = ",P2(a,b))
print("S2 = ",S2(a,b))
