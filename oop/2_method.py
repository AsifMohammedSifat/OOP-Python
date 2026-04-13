class Phone:
    def __init__(self):
        print("I am Constructor")
    def __del__(self):
        print("I am destructor")
    def display(self):
        print("I am method")

def outside_func():
    print("I am outside fucniton")

Phone.outside_func = outside_func

p = Phone()
p.display()

print(Phone.__dict__.keys())