class Company:
    def __init__(self,name,location):
        self.name = name 
        self.location = location 
    def company_details(self):
        print(f"Company Name: {self.name} Location: {self.location}")

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def personal_details(self):
        print(f"Person Name: {self.name} Age: {self.age}")
    

class Employee(Person,Company):
    def __init__(self, pname, age,cname,location):
        Person.__init__(self,pname, age)
        Company.__init__(self,cname, location)


joy = Employee('A',5,'B','ABC')
joy.personal_details()
joy.company_details()

