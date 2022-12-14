# Hàm tính giai thừa theo giải thuật đệ qui 
def giaithua(n):
    if n==1:
        return 1 
    else:
        return(n*giaithua(n-1))
number1 = 5
number2 = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của ",number1, "la", giaithua(number1))
print("Giai thừa của ", number2, "la",giaithua(number2))