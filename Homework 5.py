# Game: Heads or Tails
# This program will have a user enter heads or tails
# The computer will then generate 0 or 1, which will be heads or tails.
# Then the computer will report if the user is correct or incorrect.
# The program will then ask the user if they want to play again.
#
#
# Homework 5
# Zachary Baltrus
#
#CIS 1400

# This line is so that the computer can have a random integer.

import random

# Here is where the program will define the loop values with 0.

gameLoop = 0
playAgainLoop = 0

# This is the first loop for the game.

while gameLoop == 0:

    playAgainLoop = 0

    # This is where the computer will randomly generate a number.
     
    for computersRange in range (0,1):
        computersChoice = random.randint(0,1)

        if computersChoice == 0:
            computersChoice = "heads"

        else:
            computersChoice = "tails"

    # This is where the user will enter their choice.

    userInput = input("Please enter heads or tails: ")

    # This decieds if the player was right or wrong.

    if userInput == computersChoice:
        print("You were correct, it was " + computersChoice + "!")

    else:
        print("You guessed wrong! It was " + computersChoice + ".")

    # This is the loop that asking if the player wants to run the program again.

    while playAgainLoop == 0:

        playAgainInput = input("Would you like to play again?: (y/n) ")

        if playAgainInput == "y" or playAgainInput == "yes":
            gameLoop = 0
            playAgainLoop = 1

        elif playAgainInput == "n" or playAgainInput == "no":
            gameLoop = 1
            playAgainLoop = 1
            print("Thanks for playing!")

        else:
            playAgainLoop = 0
            print("Please enter yes or no.")
    

