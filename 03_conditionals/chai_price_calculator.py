cup_size = input("Choose your cup size (small/medium/large): ").lower()

if cup_size == "small":
    print("The price of a small cup of chai is 10 rupees.")
elif cup_size == "medium":
    print("The price of a medium cup of chai is 15 rupees.") 
elif cup_size == "large":
    print("The price of a large cup of chai is 20 rupees.")
else:
    print("Unknown cup size. Please choose small, medium, or large.")   