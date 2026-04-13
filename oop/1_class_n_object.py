class Phone:
    def __init__(self):
        print("I am Constructor")
    def __del__(self):
        print("I am destructor")
    def display(self):
        print("I am method")


p = Phone()
p.display()

print(Phone.__dict__.keys())