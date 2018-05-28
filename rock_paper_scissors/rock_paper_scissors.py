# Import libraries
from random import randint

# print choices
print("rock")
print("paper")
print("scissors")

# Input by the player
player_choice = input("Enter your choice: ").lower()

# Decide the choice by computer
random_num = randint(0, 2)
if random_num == 0:
    computer_choice = "rock"
elif random_num == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

# print(player_choice, computer_choice)

# Game logic
if player_choice == computer_choice:
    print("Its a tie!!")
elif player_choice == 'rock':
    if computer_choice == 'paper':
        print("computer wins!!")
    elif computer_choice == 'scissors':
        print("you win!!")
elif player_choice == 'paper':
    if computer_choice == 'rock':
        print("you win!!")
    elif computer_choice == 'scissors':
        print("computer wins!!")
elif player_choice == 'scissors':
    if computer_choice == 'paper':
        print("you win!!")
    elif computer_choice == 'rock':
        print("computer wins!!")
else:
    print("something not correct!!!")
