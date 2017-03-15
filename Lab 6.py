# Electrical Engineering Problem
# This program will calculate the power by having
# the user enter the current of the resistance
#
#
# Lab 6
# Zachary Baltrus
#
# CIS 1400

# First this is defining all of the Lists to be set to their base value
resistanceList = [16, 27, 39, 56, 81]
currentList = []
powerList = []

# This line is having the user enter the current values
for num in range(0, len(resistanceList)):
    print("Please enter the current of the resistance for", resistanceList[num], ":")

    currentInput = eval(input())
    if currentInput <= 0:
        print ("You cannot enter a negative number.")
        while currentInput <= 0:
            print("Enter another current input.")
            currentInput = 0
    currentList.append(currentInput)

# This for loop is for calcuating the power 5 times
for num in range(0, len(currentList)):
    powerList.append(resistanceList[num] * currentList[num]**2)

# This will be printing the table for the Current and Power
print("Resistance", "\t", "Current", "\t", "Power")
for num in range(0, len(powerList)):
    print(resistanceList[num], "\t\t", currentList[num], "\t\t", powerList[num])
    


    
    
