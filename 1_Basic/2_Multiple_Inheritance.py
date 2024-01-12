class company:
    def __init__(self, cname, location):
        self.cname = cname
        self.location = location

    def company_details(self):
        print("Company Name =", self.cname, "Location =", self.location)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_details(self):
        print("Name =", self.name, "Age =", self.age)

class employee(company, person):

    def __init__(self, emp_name, emp_age, comp_name, comp_location):
        # Initialize the parent classes separately.
        person.__init__(self, emp_name, emp_age)
        company.__init__(self, comp_name, comp_location)

    def details(self, salary, skill):
        print("Salary:", salary, "Skill:", skill)

# When creating an employee object, provide values for both company and person attributes.
ob_employee = employee("Asif", 25, "Google", "USA")

ob_employee.details(1500000, "Python OOP")

ob_employee.person_details()
ob_employee.company_details()


===============================================================================
#C++
""" 1. In C++, Function name must be different in diffent class. Otherwise if there has same named function 
and we want to access them; then Get Ambigious Message. """
#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    Person(const string& pname, int age) : pname(pname), age(age) {}

    void detail() {
        cout << "Name = " << pname << " Age = " << age << endl;
    }

private:
    string pname;
    int age;
};

class Company {
public:
    Company(const string& cname, const string& location) : cname(cname), location(location) {}

    void details() {
        cout << "Company Name = " << cname << " Location = " << location << endl;
    }

private:
    string cname;
    string location;
};

class Employee : public Person, public Company {
public:
    Employee(const string& pname, int age, const string& cname, const string& location)
        : Person(pname, age), Company(cname, location) {}
};

int main() {
    Employee empObj("Salauddin", 27, "Google", "USA");
    empObj.detail();

    return 0;
}
