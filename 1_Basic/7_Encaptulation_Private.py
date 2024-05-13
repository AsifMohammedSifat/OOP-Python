'''
    Encaptulation Access Modifier.
    Ans: Public , Private , Protected
    How to create Private member?
'''

class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id #private variable
    def details(self):
        print("Name=",self.name,"ID=",self.__id)



obStudent = student("Asif",25)
# print(object.__id) #show error
print("Before Re-assign")
obStudent.details()

print("After Re-assign")
obStudent.__id = -30 #re-assign and dont show any error.but variable is private thats why it create a new object
obStudent.details()  #id didnot change. still.id=25

print(obStudent.__dict__)


======
C++:
======

#include <bits/stdc++.h>
using namespace std;

class Student{
    
    private:
    string name;
    int id;

    public:
    void setter(string name,int id){
        this->name = name;
        this->id = id;
    }
    
    void getter(){
        cout<<"Name = "<<name<<" "<<"ID = "<<id<<endl;
    }
};

int main()
{
    Student obj;
    obj.setter("Alvi",5);
    obj.getter();


    return 0;
}


