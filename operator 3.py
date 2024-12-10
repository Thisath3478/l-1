#medical
medical = input("Enter your medical yes or no:")
attendence = int(input("Enter your attendance:"))
if medical == "YES":
    print ("Yes you are allowed")
else:
    if attendence > 75:
        print ("Yes you are allowed")
    else:
        print ("No you are not allowed")

#bike or car
print ("Please select your choise")
print ("1 is bike")
print ("2 is car")
choice = int (input("Enter your choice"))
if choice == 1:
    print ("What type of bike do you want?")
    print ("1.Kawasaki ninja H2R")
    print ("2.Luxury bike")
    choice2 = int(input("Enter your choice"))
    if choice2 == 1:
        print ("You have selected the, Kawasaki ninja H2R")
    else :
        print ("You have selected the luxury bike")
else :
        print ("What type of car do you want?")
        print ("1.Rols Royce Specter")
        print ("2.Lakyan Hyper sport")
        choice2 = int(input("Enter your choice"))
        if choice2 == 1:
            print ("You have selected the, Rols Royce Specter")
        else :
            print ("You have selected the, Lakyan Hyper sport")


#unit
unit= int(input("Please enter the unit"))
if unit<50:
    amount=unit*2.60
elif unit<=100:
    amount=unit*3.50
print(amount)