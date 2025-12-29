menu = [
    "Masala Chai",
    "Ginger Chai",
    "Lemon Tea",
    "Cold Coffee",
    "Hot Chocolate"
]

iced_tea = [my_tea for my_tea in menu if  len(my_tea) > 12]

print(iced_tea)

