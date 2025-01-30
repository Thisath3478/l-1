import random

def guess ():
    print ("welcome to the Number Guessing game")
    a = random.randint (1, 10)
    attempt = 0

    while True:
        try :
            b = int ("Guess any number from 1 to 10")
            attempt  +=1
            if b <1 or b>10:
                print ("please enter a number from 1 to 10")
                continue
            if b<a:
                print ("Too low")
            elif b>a : 
                print ("too High")
            else :
                print (f"yay you got it right in {attempt} attempts")
                break
        except ValueError:
            print ("Invalid Input")
              
guess()