""" 
Abstract class dont have body
We cannot create object of abstract classs

"""

# senior-> Project->Database
#           |
# dekstop         mobile
# login           login


from abc import ABC,abstractmethod
class Project(ABC):
    def details(self):
        self.balance =50
        print("I am core project")
    @abstractmethod
    def security(self):
        pass
class App(Project):
    def security():
        pass
    def details(self):
        print("I am from app")

b = Project()
print(b.balance)


============================================================
#C++
#include <iostream>
using namespace std;
class Project {
public:
    Project() : balance(50) {}

    virtual void details() {
        balance = 50;
        cout << "I am core project" << endl;
    }

    virtual void security() = 0;  // Pure virtual function

    int getBalance() const {
        return balance;
    }

private:
    int balance;
};

class App : public Project {
public:
    void security() override {
        // Implementation of the pure virtual function
    }

    void details() override {
        cout << "I am from app" << endl;
    }
};

int main() {
    Project* b = new App();
    b->details();

    cout << "Balance: " << b->getBalance() << endl;

    delete b;

    return 0;
}

""" 1. Virtual Keyword is mainly used in the context of polymorphism, specifically for virtual functions & virtual inheritance.
   
     2. Declare a function as virtual in a base class, this indicate to the compiler that this function may be overridden by derived classes. This enables dynamic dispatch, allowing the correct function to be called based on the actual type of the object at runtime.
"""
==========================================================================================================================
from abc import ABC, abstractmethod

class Shape(ABC):  # Define an abstract class using ABC

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Attempting to create an instance of the abstract class Shape will raise a TypeError.
# shape = Shape()  # This will result in an error.

# Creating instances of concrete subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calling methods on concrete subclasses
print("Circle Area:", circle.area())        # Output: 78.5
print("Rectangle Area:", rectangle.area())    # Output: 24

======
C++:
======
#include <iostream>
using namespace std;

// Abstract class
class Shape {
public:
    // Pure virtual function (abstract method)
    virtual void draw() = 0;

    // Concrete method
    void displayInfo() {
        cout << "This is a shape." << endl;
    }
};

// Concrete subclass Circle
class Circle : public Shape {
public:
    // Implementation of draw method
    void draw() override {
        cout << "Drawing a circle." << endl;
    }
};

// Concrete subclass Rectangle
class Rectangle : public Shape {
public:
    // Implementation of draw method
    void draw() override {
        cout << "Drawing a rectangle." << endl;
    }
};

int main() {
    // Create objects of concrete subclasses
    Circle circle;
    Rectangle rectangle;

    // Call draw method (abstraction)
    circle.draw();      // Output: Drawing a circle.
    rectangle.draw();   // Output: Drawing a rectangle.

    // Call concrete method
    circle.displayInfo();      // Output: This is a shape.
    rectangle.displayInfo();   // Output: This is a shape.

    return 0;
}


