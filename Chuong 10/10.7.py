# Sử dụng hàm string
s = "a b c d e f duck"
s_sub = "d"
s_find = "duck"
s_replace = "dog"
print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:",str.strip(s))
print("Chuỗi với kí tự đầu chuỗi viết hai: ",str.capitalize(s))
print("Số lần s_sub xuất hiện trong s: ",str.count(s, s_sub))
print("Chuỗi s sau khi thay thế và tìm kiếm là: ",str.replace(s, s_find, s_replace,))