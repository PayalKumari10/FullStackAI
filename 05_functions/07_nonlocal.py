chai_type = "Masala"

def update_order():
    chai_type = "Chai"  

    def kitchen():
        nonlocal chai_type
        chai_type = "Cardamom"
    kitchen()
    print("After kitchen update", chai_type)

update_order()
