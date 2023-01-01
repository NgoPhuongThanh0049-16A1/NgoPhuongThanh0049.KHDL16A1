# Tuple strings
color = ("red", "green", "yellow", "blue", "white", "pink", "orange", "red", "blue")
x = int(input("Nhập số từ 0 đến 9: "))
y = int(input("Nhập số từ -1 đến -9: "))
z = str(input("Nhập chuỗi cần tìm: "))
print("Tuple", "[", x, "]", "=", color[x])
print("Tuple", "[", y, "]", "=", color[y])
print(z, "xuất hiện trong tuple ", color.count(z), "lần")
