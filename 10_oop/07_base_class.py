class Chai:

    def __init(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai) :
#       def __init__(self, type_, strength, spice_level):
#          self.type = type_
#          self.strength = type_
#          self.strength = strength
#          self.spice_level = spice_level


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level










class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
        print(f"Chai created | Type: {self.type}, Strength: {self.strength}")


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
        print(
            f"GingerChai created | Type: {self.type}, "
            f"Strength: {self.strength}, Spice Level: {self.spice_level}"
        )


# object creation
chai = GingerChai("Ginger", "Strong", "High")
