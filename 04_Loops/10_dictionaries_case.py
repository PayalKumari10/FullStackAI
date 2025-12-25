users = [
    {"id": 1, "total": 100, "coupon": "P28"},
    {"id": 2, "total": 150, "coupon": "F45"},
    {"id": 3, "total": 200, "coupon": "Z99"},
]

discounts = {
    "P28": (0.10, 0),
    "F45": (0.15, 0),
    "Z99": (0, 20),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount_amount = user["total"] * percent + fixed
    final_amount = user["total"] - discount_amount
    print(f"User ID: {user['id']}, Original Total: Rs.{user['total']}, Discount: Rs.{discount_amount}, Final Amount: Rs.{final_amount}")