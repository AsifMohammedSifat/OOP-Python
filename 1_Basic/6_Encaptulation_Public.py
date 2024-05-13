'''
    What is Encaptulation?
    Ans: Data and Method are binding in a single unit.
    Encaptulation = single unit(data + method)
'''


class student:
    def __init__(self,name,id):
        self.name = name  #data
        self.id = id
    def details(self):    #method
        print("Name=",self.name,"ID=",self.id)


obStudent = student("Rahim",25)

print("Before Re-assign")
obStudent.details()

print("After Re-assign")
obStudent.id = -30 #reassign and dont show any error

obStudent.details()



======
C++:
======

#include <bits/stdc++.h>
using namespace std;

class Student{
    
    public:
    string name;
    int id;

    Student(string name,int id){
        this->name = name;
        this->id = id;     
    }
    void details(){
        cout<<"Name = "<<name<<" "<<"ID = "<<id<<endl;
    }
};

int main()
{
    Student obj("Avi",5);
    obj.details();
    obj.id = 1;
    obj.name = "Akash";
    obj.details();


    return 0;
}
