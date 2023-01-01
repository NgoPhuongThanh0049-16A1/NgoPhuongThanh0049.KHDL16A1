# List numbers 1 
numbers1 = []

while True:
    a = input('Nhập dữ liệu: ')
    b = input(" Tiếp tục nhập giá trị? 1: Có, 0: Không ")
    if  b == '0':
        print('Kết thúc')
        break
    numbers1.append(a)
   
print("List:", numbers1)
x = int(input("Nhập giá trị cần tìm x: "))
print('Tổng các giá trị trong list:',len(a))
print('%i xuất hiện %i lần trong list'%(x,a.count(x)))
d=[]
for i in a:
    if x<i:
        d=d+[i]
print('Các số lớn hơn %i trong list:'%(x),d)