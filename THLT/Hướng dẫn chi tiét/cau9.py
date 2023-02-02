a, b, c = map(float,input('Xin mời nhập độ dài 3 cạnh: ').split())
cv = a+b+c
p = cv/2; import math
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Chu vi tam giác là {cv:.2f}')
print(f'Diện tích tam giác là: {s:.2f}')