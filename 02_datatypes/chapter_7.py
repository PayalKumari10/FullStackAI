masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, and {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ginger to cardamom ratio G: {ginger_ratio} and C:{cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ginger to cardamom ratio G: {ginger_ratio} and C:{cardamom_ratio}")


# membership
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cardamom in masala spices? {'cardamom' in masala_spices}")
print(f"Is 'clove' not in masala spices? {'clove' not in masala_spices}")    
