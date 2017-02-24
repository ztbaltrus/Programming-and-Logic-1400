# Financial application: compair loans with various interest rates.
# This program will go over for loops and while loops
# The code will have the user enter a loan amount and the number of years they will have
# the loan for.
#
#
# Homework 4: Loop HW
#
# Name: Zachary Baltrus
# CIS 1400

# Setting the value of all of the variables for the loops.

# Im using this so the program can step up 1/8th
def loanrange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

# This is setting all of the base values for the loop statements

continueLoop = 0
loanAmount = 1
numberOfYears = 1
interestRate = loanrange(5,8.125,.125)

# Calling the first while loop so that the user could run the
# program again if they want to.

while continueLoop == 0:

    print("\n\n\n\tFinancial Application\n\n\n")

    if continueLoop == 0:
        
        # The next while loop would be to call the loan amount.
        # The reason it will be a loop is so that if the user
        # entered a number lower than 0, the loan amount input
        # would restart.
        
        while loanAmount != 0:
            loanAmount = eval(input("Loan Amount: "))

            if loanAmount <= 0:
                loanAmount = 1
                print("Please enter a positive number")

            else:
                
                # This while loop will be for the number of years
                # input. Again, if the user enters a number under
                # 0 the number of years loop will restart.
                
                while numberOfYears != 0:
                    numberOfYears = eval(input("Number of Years: "))

                    if numberOfYears <= 0:
                        numberOfYears = 1
                        print("Please enter a positive number")

                    elif numberOfYears >= 0:
                        print("Interest Rate : Monthly Payment : Total Payment")
                        for loanRates in interestRate:

                            monthlyLoanRate = loanRates / 1200

                            monthlyPayment = loanAmount * monthlyLoanRate / (1
                                - 1 / (1 + monthlyLoanRate) ** (numberOfYears * 12)) 
                            totalPayment = monthlyPayment * numberOfYears * 12

                            monthlyPayment = int(monthlyPayment * 100) /100
                            totalPayment = int(totalPayment * 100) / 100


                            print("%.3f" % loanRates, "\t\t", "%.2f" % monthlyPayment, "\t", "%.2f" % totalPayment)

                            if loanRates == 8:
                                numberOfYears = 0
                                loanAmount = 0
                                continueLoop = 1



    if continueLoop == 1:
        
        runAgain = input("Run the program again?: y/n ")
        if runAgain == "y" or runAgain == "yes":
            continueLoop = 0
            numberOfYears = 1
            loanAmount = 1
            interestRate = loanrange(5,8.125,.125)

    else:
        break
