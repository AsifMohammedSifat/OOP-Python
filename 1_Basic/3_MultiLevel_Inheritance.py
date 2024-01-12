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
# GrandFather - 5 crore
#       |
# Father - 3 crore
#       |
# Ami - 2 crore

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

========================================================================================
#C++
#include <iostream>
using namespace std;

class GrandFather {
public:
    void property() {
        cout << "I have 5 crore taka" << endl;
    }
};

class Father : public GrandFather {
public:
    void property() {
        cout << "I have 3 crore taka" << endl;
    }

    void father() {
        GrandFather::property();
    }
};

class Child : public Father {
public:
    void property() {
        cout << "I have 2 crore taka" << endl;
    }

    void father() {
        Father::property();
    }

    void grandFather() {
        Father::father();
    }
};

int main() {
    Child ami;
    ami.property();
    ami.father();
    ami.grandFather();

    return 0;
}
