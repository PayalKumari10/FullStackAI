def food_customer():
    print("Welcome! What food would you like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = food_customer()
next(stall) # start the generator 

stall.send("Special Thali")
stall.send("Dinner Thali")

