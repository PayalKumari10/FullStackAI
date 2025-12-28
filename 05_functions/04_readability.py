def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 20)

print(my_bill)

print("Order for table 2:", calculate_bill(5, 15))