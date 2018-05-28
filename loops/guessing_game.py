# Import libraries
from random import randint

# generate a random number
random_number = randint(1, 10)

number = None

# loop through the number
while number != random_number:
    # guess a number
    number = int(input("Guess a number: "))
    # print(number, random_number)
    if number > random_number:
        print("Guess is too high")
    elif number < random_number:
        print("Guess is too low")
    else:
        print("Correct guess")
