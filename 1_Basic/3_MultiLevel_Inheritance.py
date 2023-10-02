class Grandparent:
    def __init__(self) -> None:
        pass
    def property(self):
        print("I have 5 corer Taka")

class Parent(Grandparent):
    def __init__(self) -> None:
        super().__init__()
    

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()

ami = Child()
ami.property()





#Example-02


class Grandparent:
    def __init__(self) -> None:
        pass
    def property(self):
        print("I have 5 corer Taka")

class Parent(Grandparent):
    pass
    def property(self):
        print("I have 3 corer Taka") 
    def father_property(self):
        super().property()  

class Child(Parent):
    pass
    def property(self):
        print("I have 2 corer Taka")
    def father_property(self):
        super().property()
    def gfather_property(self):
        super().father_property()

ami = Child()
ami.property()
ami.father_property()
ami.gfather_property()
