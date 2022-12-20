# sử dụng hàm datetimes
x = int(input("Nhập ngày: "))
y = int(input("Nhập tháng: "))
z = int(input("Nhập năm: "))
from datetime import datetime
print("Ngày tháng năm vừa nhập: ", x,"-", y,"-",  z )
# Kiểm tra năm nhuận 
if ((z%4==0) and (z%100!=0) or (z%400==0)):
    print("Năm ",z , "là năm nhuận")
else:
    print("Năm", z, "không là năm nhuận ")
# Kiểm tra ngày tháng năm là thứ mấy 
import calendar
calendar.weekday(z, y, x)
if calendar.weekday(z, y,x)==0:
    print(x,"-", y, "-", z ,"là thứ Hai")
elif calendar.weekday(z, y,x)==1:
    print(x,"-", y, "-", z ,"là thứ Ba")
elif calendar.weekday(z, y,x)==2:
    print(x,"-", y, "-", z ,"là thứ Tư")
elif calendar.weekday(z, y,x)==3:
    print(x,"-", y, "-", z ,"là thứ Năm")
elif calendar.weekday(z, y,x)==4:
    print(x,"-", y, "-", z ,"là thứ Sáu")
elif calendar.weekday(z, y,x)==5:
    print(x,"-", y, "-", z ,"là thứ Bảy")
else:
    print(x,"-", y, "-", z ,"là Chủ Nhật")

# Kiểm tra tháng nhập vào có bao nhiêu ngày 
import calendar 
print(" Số ngày trong tháng là: ",  calendar.monthrange(z,y))

        


        

        