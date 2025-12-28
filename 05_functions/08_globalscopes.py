chai_type = "Plain"   #global scope

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Kesar Chai"
    kitchen()

front_desk()
print("Final global chai:", chai_type)        