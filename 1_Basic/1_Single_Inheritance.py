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

==============
C++
==============
#include <iostream>
#include <string>
using namespace std;

class Animal
{
protected:
    string name;

public:
    Animal(string name)
    {
        this->name = name;
    }

    void eat()
    {
        cout << name << " is eating" << endl;
    }
};

class Cat : public Animal
{
public:
    // way-1
    Cat(string name) : Animal(name)
    {
        //No need to initialize 'name' again; it's already done in Animal's constructor
    }

    // way-2
    // Cat(string name)
    // {
    //     this->name = name; // Assign name in the body of the Cat constructor
    // }
};

int main()
{
    Cat cat("Cat");
    cat.eat();
    return 0;
}
