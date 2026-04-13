class Animal:
    def __init__(self,name):
        self.name = name 
    def eat(self):
        print(f"{self.name} can eat")


class Cat(Animal):
    def sound(self):
        print("Meow") 

class Dog(Animal):
    def __init__(self,name,age):
        self.age = age 
        super().__init__(name)
        # Animal.__init__(self,name)
    def sound(self):
        print("Barking") 

kitty = Cat("Kitty")
kitty.eat();

tom = Dog("Tom",5)
tom.eat()