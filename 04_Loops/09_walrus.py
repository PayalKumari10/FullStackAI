# value = 15

# remainder = value % 5

# if remainder:
#     print(f"Not divisible by 5, remainder is {remainder}")




value = 17

if (remainder := value % 5):
    print(f"Not divisible by 5, remainder is {remainder}")

# available_sizes = ["S", "M", "L", "XL"]

# if (requested_size := input("Enter your chai cup size:")) in available_sizes:
#     print(f"{requested_size} size is available.")
# else:
#     print(f"Sorry, {requested_size} size is not available.")  


    flavors = ["Masala", "Ginger", "Cardamom", "Tulsi"]

    print("Available flavors:", flavors)

    while (flavor := input("Choose your flavor: ")) not in flavors:
        print("Invalid flavor, please choose again.")

print(f"You have selected {flavor} flavor. Enjoy your chai!")