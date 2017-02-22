# Count positive and negative numbers
# Lab 4: Loop Lab
#
#
# Zachary Baltrus


# This is setting all values at 0 and setting the guess value at 1.
guess = 1
howmany = 0
sumNum = 0
pos = 0
neg = 0


# This is the start of the while loop
while guess != 0:
    guess = eval(input("Enter an integer, the input ends if it is 0: "))
    #This line will determin wether or not the user enterd any other numbers besides 1
    if guess == 0 and howmany == 0:
        print("You didnt enter any numbers")
    #This will sum all the numbers up
    elif guess == 0:
        avg = (sumNum / howmany)
        print("The number of positives are ", pos)
        print("The number of negatives are ", neg)
        print("The total is ", howmany)
        print("The average is ", avg)
    #This will add a positive number and an input to the corisponding values
    elif guess > 0:
        howmany += 1
        pos += 1
    #This will add a negative number and an input to the corisponding values
    else:
        howmany += 1
        pos += 1
        
    
