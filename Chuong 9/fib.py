 # hàm fibonacy
def fib(n):
    if n== 0 or n==1: return n 
    else:
        return fib(n-1) + fib(n-2)
x = int(input("Nhập giá tị x="))
print("fibonacy(",x,"=",fib(x))