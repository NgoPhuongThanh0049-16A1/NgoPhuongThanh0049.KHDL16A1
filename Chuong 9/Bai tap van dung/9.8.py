# Kiểm tra 1 số có phải là số hoàn hảo 
a = eval(input("Nhập số: "))
tong = 0
for i in range(1,a-1):
    if (a%i==0):
        tong+=i
if (tong==a):
         print(a,"là số hoàn hảo")
else:
        print(a,"là số không hoàn hảo")