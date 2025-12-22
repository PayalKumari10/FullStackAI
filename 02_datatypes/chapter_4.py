is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling #upcasting
print(f"Total actions (boiling * stri count): {total_actions}")

milk_present = 11 # no milk
print(f"Is milk present? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can we serve chai? {can_server}")