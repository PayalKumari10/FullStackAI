tea_prices_inr = {
    "Masala Chai": 30,
    "Ginger Chai": 25,
    "Lemon Tea": 20,
    "Cold Coffee": 50,
    "Hot Chocolate": 45     
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)