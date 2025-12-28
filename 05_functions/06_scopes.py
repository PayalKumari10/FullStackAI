def server_chai():
    chai_type = "Masala Chai" #local scope
    print(f"Inside function {chai_type}")


chai_type = "Ginger Chai" #global scope
server_chai()   
print(f"Outside function {chai_type}")


def chai_counter():
    chai_order = "Ginger Chai" #Enclosing scope
    def print_order():
        chai_order = "Masala Chai" 
        print(f"Inner:", chai_order)
    print_order()    
    print("Outer: ", chai_order)    

chai_order = "Tulsi" #Global
chai_counter()
print("Global: ", chai_order)