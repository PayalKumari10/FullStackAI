def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200, 250]

for price in orders:
    final_amount = add_vat(price, 20)
    print(f"Original: {price}, Final with VAT: {final_amount}")
