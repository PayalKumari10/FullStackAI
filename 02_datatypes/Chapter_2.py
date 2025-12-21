# Muttable Data Types: Set can be change
spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Turmeric")
spice_mix.add("Cumin")
spice_mix.add("Coriander")
print(f"Spice mix after additions: {spice_mix}")
print(f"Spice mix after additions id: {id(spice_mix)}")

# Output:
# Initial spice mix id: 2265188139744
# Initial spice mix id: set()
# Spice mix after additions: {'Coriander', 'Cumin', 'Turmeric'}
# Spice mix after additions id: 2265188139744