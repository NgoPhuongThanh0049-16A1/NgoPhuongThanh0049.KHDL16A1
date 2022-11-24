# Tính và in ra kết quả  của biểu thức 
import math #note: dùng công thức tính toán phải dùng "import math"
n = int(input("Nhập số nguyên: "))
x = int(input("Nhập số thực: "))
A = (x**2 + x + 1)**n +(x**2 - x + 1)**n
print("Kết quả là:",A)
