seat_type = input("Enter seat type(sleeper/AC/general/luxary) ").lower()

match seat_type:
    case "sleeper":
        print("Sleepar- Non Ac, beds available")
    case "ac":
        print("AC- Ac, beds available")
    case "general":
        print("General- Non Ac, no beds available")
    case "luxary":
        print("Luxary- Premium seat with Meal")
    case _:
        print("Invalid seat type")