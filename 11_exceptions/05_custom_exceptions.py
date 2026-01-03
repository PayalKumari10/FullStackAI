def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavor")
    print(f"Brewing {flavor} chai...")

brew_chai("mint")



# Output :
#   brew_chai("mint")
#     ~~~~~~~~~^^^^^^^^
#   File "d:\FullStackAI\11_exceptions\05_custom_exceptions.py", line 3, in brew_chai
#     raise ValueError("Unsupported chai flavor")
# ValueError: Unsupported chai flavor
