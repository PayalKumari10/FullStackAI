def make_chai():
    #return "Here is your masala chai"
    print("Here is your masala chai")

return_value = make_chai()

print(return_value)    
    
def idle_chaiwala():
        pass

print(idle_chaiwala())

def sold_cups():
      return 120

total = sold_cups()
print(total)

def chai_status(cup_left):
    if cup_left > 0:
        return "Chai is available"
    return "Chai is sold out"    
    print("chai")

print(chai_status(0))
print(chai_status(5))

def chai_report():
     return 100, 20, 10 #sold, remaining, not_paid

sold, remaining, not_paid = chai_report()
print("Sold:", sold)
print("Remaining:", remaining)