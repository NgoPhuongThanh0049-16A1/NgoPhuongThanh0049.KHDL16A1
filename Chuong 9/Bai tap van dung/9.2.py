# Tính năm âm lịch 
can=["Canh","Tân","Nhâm","Quý","Giáp","Át","Bính","Đinh","Mậu","Kỳ"]
chi=["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
nam=int(input("Nhập năm :"))
c=nam%10
ch=nam%12
print("Năm", nam,"lịch âm là năm",can[c]+" "+chi[ch])