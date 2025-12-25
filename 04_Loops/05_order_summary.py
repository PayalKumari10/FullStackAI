names = ["Payal", "Saumya", "Raman", "Ankit", "Neha"]

bills = [50, 60, 70, 80, 90]

for  name, amount in zip(names, bills):
    print(f"Dear {name}, your total bill amount is Rs.{amount}.")