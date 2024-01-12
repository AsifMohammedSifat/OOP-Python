""" Hierarchical Inheritance: """

class Parent:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Parent's name is {self.name}")

class Child1(Parent):
    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby

    def show_info(self):
        super().show_info()
        print(f"Child1's hobby is {self.hobby}")

class Child2(Parent):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def show_info(self):
        super().show_info()
        print(f"Child2 goes to {self.school}")

# Creating instances of the classes
parent = Parent("John")
child1 = Child1("Alice", "Painting")
child2 = Child2("Bob", "XYZ School")

# Calling the show_info method on instances
parent.show_info()  # Output: Parent's name is John
child1.show_info()  # Output: Parent's name is Alice, Child1's hobby is Painting
child2.show_info()  # Output: Parent's name is Bob, Child2 goes to XYZ School


# Cat-> sound + eat

class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(f"{self.name} can eat")

class Cat(Animal):
    def __init__(self,name) -> None:
        # super().__init__(name)
        Animal.__init__(self,name)
    # def eat(self):
    #     print(f"{self.name} can eat")
    def sound(self):
        print(self.name," sounds like Meeow!")
    
    def __repr__(self) -> str:
        return f"{self.name} class"

class Dog(Animal):
    # def __init__(self,name) -> None:
    #     self.name = name
    # def eat(self):
    #     print(f"{self.name} can eat")
    def sound(self):
        print(self.name," sounds like Bark!")


c = Cat("Cat")
c.eat()
d = Dog("Dog")
d.eat()

print(c)



=======================================================================================
#In C++

class Animal {
public:
    Animal(const string& name) : name(name) {} #Constructor

    void eat() const {
        cout << name << " can eat" << endl;
    }

protected:
    string name;
};

class Cat : public Animal {
public:
    Cat(const string& name) : Animal(name) {} #Constructor

    void sound() const {
        cout << name << " sounds like Meeow!" << endl;
    }
};

class Dog : public Animal {
public:
    Dog(const string& name) : Animal(name) {} #Constructor

    void sound() const {
        cout << name << " sounds like Bark!" << endl;
    }
};

int main() {
    Cat("Cat").eat();
    Dog("Dog").eat();

    return 0;
}
