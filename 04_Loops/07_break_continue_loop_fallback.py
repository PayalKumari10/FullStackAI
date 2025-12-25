flavours = ["Masala", "Ginger", "Cardamom", "Tulsi","Out of stock", "Discontinued", "Elaichi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
       print(f"{flavour} item food")
       break
    print(f"Preparing {flavour} chai")

print(f"Out side of loop")