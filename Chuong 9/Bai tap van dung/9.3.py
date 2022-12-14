#Tính chỉ số BMI
a = eval(input("Nhập cân nặng(kg): "))
b = eval(input("Nhập chiều ccao(m): ")) 
c = float(a/(b*b))
if c< 18.9:
    print("Chỉ số BMI của bạn là: ",c, "Bạn gầy")
elif 18.5<c<24.99:
    print("Chỉ số BMI của bạn là: ",c, "Bạn bình thường " )
else:
    print("Chỉ số BMI của bạn là: ",c, "Bạn thừa cân ")