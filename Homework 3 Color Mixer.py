# Color Mixer:
# This program will prompt the user to enter the name of two primary colors
# to mix. The only colors they will be able to enter are "red" "blue" "yellow"
# If they enter anyother color then that, an error message will be displayed.
#
#
# Name Zachary Baltrus
# Assignment: Homework 3: Color Mixer
#
# CIT 1400


# This line of code will as the user to enter their first color choice
colorChoice1 = input("Please input a primary color. (red, blue, or yellow): ")

# This next line of code will ask the user for their second color choice
colorChoice2 = input("Please select another primary color. (red, blue, or yellow): ")

# This line of code will be if the user enters
# the same color. This will result in an NameError.
if colorChoice1 == colorChoice2:
    print("Please enter two differnt colors.")

# The rest of the else if statements are all of the possilble
# outcomes when the user chooses two different primary colors.

elif colorChoice1 == "red" and colorChoice2 == "blue":
    resultColor = "purple."
    
elif colorChoice1 == "red" and colorChoice2 == "yellow":
    resultColor = "orange."

elif colorChoice1 == "blue" and colorChoice2 == "yellow":
    resultColor = "green."

elif colorChoice1 == "blue" and colorChoice2 == "red":
    resultColor = "purple."

elif colorChoice1 == "yellow" and colorChoice2 == "red":
    resultColor = "orange."

elif colorChoice1 == "yellow" and colorChoice2 == "blue":
    resultColor = "green."

# This else statement will be if the user enters any colors
# that are not of the three primary colors. This will then
# result in a NameError.
else:
    print("Error, please enter primary colors.")

# Finally this line of code will order all of the color
# choices together and create a organized sentence.
print("When you mix", colorChoice1, "and", colorChoice2 + ", you get " + resultColor)
