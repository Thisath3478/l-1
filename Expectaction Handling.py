try:
    num = int(input("enter your number:"))
    print (num)
    expect ValueError as ex:
        print("Exception: ",ex) 


valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n%2 == 0:
            print("bye")
        valid = True
    except ValueError:
        print("Invalid")



try:
    num1= int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("The exception is ",ex)
except:
    print("Some error occurred")
finally:
    print("I will execute no matter what happens")



valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        while n%2 == 0:
            print("bye")
            valid = True
    except ValueError:
        print("Invalid")