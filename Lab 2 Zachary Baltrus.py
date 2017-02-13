# Finacials: currency exchange
# This program will be used to convert USD to RMD
# This program will consist of if statements
# 
# Name: Zachary Baltrus
# Assignment: Lab 2
#
# CIT 1400

# This line of code will have the user enter the currency exchange rate
currencyExchangeRate = eval(input("Enter the exchange rate from dollars to RMB: "))

# This line of code will have the user enter how they will want the currency converted
currencyExchangeCalculation = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

# This if statement will be if the user enters 0
if currencyExchangeCalculation == 0:
    dollarAmount = eval(input("Enter the dollar amount: "))
    print("$", dollarAmount, "is", (dollarAmount * currencyExchangeRate), "yuan")

# This if statement will be if the user enters 1
if currencyExchangeCalculation == 1:
    rmbAmount = eval(input("Enter the RMB amount: "))
    print(rmbAmount, "yuan is", "%.2f" % (rmbAmount / currencyExchangeRate))

# This else statement will be if anything othen than 0 or 1 is entered
if currencyExchangeCalculation != 0 and currencyExchangeCalculation != 1:
    print("Incorrect Input")

