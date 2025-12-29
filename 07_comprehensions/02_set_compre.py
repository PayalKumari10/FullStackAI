favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Ginger Chai", "Lemon Tea", "Green Tea", "Cardamom Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

recipes = {
    "Masla Chai": ["ginger", "cardmom", "clove"],
    "Elachi Chai": ["elachi", "saffron", "milk"],
    "Ginger Chai": ["ginger", "milk", "sugar"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)