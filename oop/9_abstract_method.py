from abc import ABC, abstractmethod

class Project(ABC):

    def details(self):
        self.balance = 50
        print("I am core project")

    @abstractmethod
    def security(self):
        pass


class App(Project):

    def security(self):
        print("App security implemented")

    def details(self):
        print("I am from app")


# b = Project() ❌ not allowed
b = App()
b.details()
b.security()