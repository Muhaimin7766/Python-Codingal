class dad:
    def __init__(self, eyes, Kind):
        self.eyes=eyes
        self.Kind= Kind
    def display(self):
        print("Your eye colour is", self.eyes)
        print("You are KInd", self.Kind)

class son(dad):
    def __init__(self, name, age, eyes, Kind):
        self.name=name
        self.age=age

        dad.__init__(self, eyes, Kind)

obj=son("Rhino", 8, "Grey", True)
obj.display()