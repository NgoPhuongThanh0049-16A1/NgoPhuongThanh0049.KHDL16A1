def giaithua(n):
    if n==1:
        return 1
    else:
        return(n*giaithua(n-1))
number = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của ", number,"là",giaithua(number))
     