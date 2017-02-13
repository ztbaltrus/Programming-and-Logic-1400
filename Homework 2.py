# Game: Rock, Paper, Scissor
# In this program we will make a Rock, Paper, Scissor game.
# This rogram will randomly generate a 0, 1, 2 representing each of the games options
#
# Name: Zachary Baltrus
# Homework 2
#
# CIT 1400

#THis string will import random
import random 

# The first code we will write will be an input string asking the player to enter a number
playersChoice = eval(input("scissor (0), rock (1), paper (2): "))


# This string will randomly generate the computers choice
for computersChoiceRange in range(0,1):
    computersChoice = random.randint(0,2)
    
#These are all of the possible outcomes while playing the game
    
# All the outcomes if the computer chose scissors
if computersChoice == 0:
    print("The computer chose scissor.")
    
    if playersChoice == 0:
        print("You chose scissor too! Its a draw!")
        
    if playersChoice == 1:
        print("You chose rock. You win!")
        
    if playersChoice == 2:
        print("You chose paper. You lose.")

# All the outcomes if the computer chose rock
if computersChoice == 1:
    print("The computer chose rock")
    
    if playersChoice == 0:
        print("You chose scissor. You lose.")
        
    if playersChoice == 1:
        print("You chose rock too! Its a draw!")
        
    if playersChoice == 2:
        print("You chose paper. You win!")

# All the outcomes if the computer chose paper
if computersChoice == 2:
    print("The computer chose paper.")
    
    if playersChoice == 0:
        print("You chose scissor. You win!")
        
    if playersChoice == 1:
        print("You chose rock. You lose.")
        
    if playersChoice == 2:
        print("You chose paper too! Its a draw!")
    
