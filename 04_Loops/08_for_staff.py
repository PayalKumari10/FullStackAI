staff = [("Payal", 22), ("Saumya", 21), ("Raman", 20)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to work as staff.")
        break
else:
    print("No eligible staff found.")    