def well_wishes():
    print("hello")
    print("how are you")
well_wishes()


def seasons():
    print("It is summer")
seasons()


def calculator():
    def add(a,b):
        return a+b
    def subscract(a,b):
        return a-b
    def divide(a,b):
        return a/b 
    def multiply(a,b):
        return a*b
    print("1.addition")
    print("2.subtraction")
    print("3.divition")
    print("4.multiply")
choice = int(input("enter your choice"))
1=int(input("enter your first number"))
2=int(input("enter your second number"))
if choice == 1:
print()