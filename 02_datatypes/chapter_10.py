chai_order = dict(type="Masala Chai", sugar_level=3, milk=True)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "sugar_level": 2, "milk": False}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardmom" : "crushed", "cloves" : "whole"}
chai_recipe.update(extra_spices)

print(f"Updated chai_recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")
print(f"Customer_note is: {customer_note}")