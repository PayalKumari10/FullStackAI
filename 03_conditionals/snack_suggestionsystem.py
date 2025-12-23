snack = input("Enter your preferred snack:").lower()

print(f"You have chosen: {snack}")

if snack == "cookies" or snack == "samosa":
    print("Great choice! Enjoy your snack with tea.")
elif snack == "chips":
    print("Chips are a bit salty, but go well with tea.")
else:
    print("Show Unavailable: We don't have that snack option. we only serve cookies or samosa with tea")
