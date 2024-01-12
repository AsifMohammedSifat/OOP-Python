""" Single Inheritance """

#example-1
class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')


class Cat(Animal):
    def speak(self):
        print(self.name," said to me hello")

cat =  Cat("Cat")

cat.eat()
cat.speak()

#Example-02
class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')
        print(self.name,"is eating 2")


class Cat(Animal):
    def __init__(self,name) -> None:
        # self.name = name              #type - 1
        # Animal.__init__(self,name)    #type - 2
        super().__init__(name)          #type - 3

    # def eat(self):
    #     print(self.name,"is eating")

cat =  Cat("Cat")

cat.eat()

==========================================================================================================
#C++ Syntax
// Base class
class Animal {
  public:
    string animal_name = "Cat";
};

// Derived class
class Cat: public Animal {
  public:
    string sound = "Meow Meow";
};

int main() {
  Cat myAnimal;
  cout << myAnimal.animal_name + " " + myAnimal.sound;
  return 0;
}
