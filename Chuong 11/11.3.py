# Tìm thú trong vườn thú 
a = str(input("Nhập con thú cần tìm: "))
zoo = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("List of animals; ",zoo)
print("Number of animals: ", len(zoo))
find = a in zoo
print("There is", a, "in of animals")
