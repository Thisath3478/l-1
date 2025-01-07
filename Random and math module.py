import random
playing=True
number = str(random.randint(10,20))
print ("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
while playing:
    guess = input("Give me your best guess! \n")
if number == guess:
    print("You win the game")
    print("The number was",number)
    break
else:
    print ("Your guess isn't quite right, try again. \n")



import random
options = ["rock","paper","scissors"]
user = input("Choose Rock, Paper, or Scissors - ")
computer = input random.choice
print("You chose:", user_choice)
print("Computer chose:", computer)
if user == computer:
    print("It's a tie!")
elif user == "Rock" and computer == "Scissors":
    print("Rock smashes scissors! You win!")
elif user == "paper" and computer == "Rock":
    print("Paper covers rock! You win!")
elif user == "Scissors" and computer == "Paper":
    print ("Scissors cut Paper! you win")
else:
    print("You lose!.")


import math
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))
print(math.ceil(45.490))
print(math.floor(45.890))
print(math.factorial(5))