# Integer 


black_tea_grams = 14
ginger_gram = 2

total_grams = black_tea_grams + ginger_gram
print(f"Total grams of tea ingredients: {total_grams} grams")

remaining_tea = black_tea_grams - ginger_gram
print(f"Remaining black tea grams after adding ginger: {remaining_tea} grams")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving} litres")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot: {bags_per_pot} bags")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods after making cups of chai: {leftover_pods} pods")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"Powerful flavour strength: {powerful_flavour}")

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {total_tea_leaves_harvested} leaves")
