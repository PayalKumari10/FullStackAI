# chai = "Ginger Chai"
 
# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)
# print(chai)


chai= [1,2,3]

def edit_chai(cup):
    cup[1] = 41

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
make_chai("Ginger", "Full Cream", "2 spoons") #postional arguments
make_chai(milk="Skimmed", sugar="No sugar", tea="Masala") #keyword arguments

def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("Cardamom", "Saffron", milk="Almond Milk", sugar="Honey")  

# def chai_order(order=[]):
#     order.append("Chai")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)
chai_order() 
chai_order() 