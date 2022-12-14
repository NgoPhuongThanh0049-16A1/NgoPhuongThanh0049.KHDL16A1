a = eval(input("Cho biết số cân(kg):  "))
b = eval(input("Cho biết chiều cao(m): "))
import math
def tinh_bmi(a, b):
    c= a/math.pow(b,2)


print("Chỉ số bmi của bạn là: %0.2f"%(tinh_bmi(a,b)))