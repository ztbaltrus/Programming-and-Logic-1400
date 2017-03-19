# Drivers License Exam
# This program will grade a drivers license exam by
# having the user enter in all of their multiple choice
# answers for each question.
#
# Homework 6
# Zachary Baltrus
#
# CIS 1400


# These two lists are set for the test answers and the users input answers
answerList = ["B", 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']
studentsChoice = []
# This is setting the base value for the question numbers and the amount right
questionNumber = 1
amountRight = 0
#These print statements are for the design aspect for the code
print("\n\n\t\tDrivers License Exam\n\n\n")
print("\tPlease only use UPPER case.\n\n")

# This for loop is grabbing each value out of the answerList Array and then creating
# and input statement and then compairing the two values to see if they match up.
for i in range(0, len(answerList)):
    print("Please enter answer choice for question", questionNumber)
    answerInput = input()
    
    if answerInput == answerList[i]:
        amountRight += 1
        questionNumber += 1
        studentsChoice.append(answerInput)
    else:
        questionNumber += 1
        studentsChoice.append(answerInput)

# This if statement is telling the user if they passed or not
if amountRight >= 15:
    print("You passed")

else:
    print("You failed")
# Then finally wether they passed or failed, the program will show the user
# ther percentage and the score they got.
print("Your score is", (amountRight/20) * 100, "%")
print("You scored", amountRight, "/20")
