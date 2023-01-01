# Xác định các bữa ăn liên tiếp có nhàm chán hay không?
meals_1 = ['Redneck Ribs', 'Peawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Peawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']

def menu_is_boring(meals):
    b= True
    for x in meals:
        if meals.count(x)!=1:
            b=False
            break
    return b
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))
