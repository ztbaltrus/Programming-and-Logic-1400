# Object Oriented Programming: Stocks
# In this program, there is going to be a class that is called stock
# the class will be full of funtions that can be used when doing stock calculations
# Then there is a main function that will use the functions in a print statement
#
# Zachary Baltrus
# Homework 11
#
# CIS 1400

# Creating the stock class
class Stock:
    # This fuctions will be what all the other functions use for making the stock
    def __init__ (self, symbol="None", name="None", previousClosingPrice=0.0, currentPrice=0.0):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    def getName(self): # Getting the stock name
        return(self.name)
    
    def getSymbol(self):# Getting the stock symbol
        return(self.symbol)

    def getPreviousPrice(self): # Getting the pervious stock price
        return(self.previousClosingPrice)

    def getCurrentPrice(self): # Getting the current stock price
        return(self.currentPrice)

    def getChangePercent(self): # Converting the change percentage 
        if self.previousClosingPrice == self.currentPrice:
            return("There is no change in stock price.")
        else:
            return("%.2f" % (((self.currentPrice - self.previousClosingPrice)/self.previousClosingPrice)*100))
        
# The main fuctions that would be all the print statements for making the program
def main():
    S = Stock("INTC", "Intel Corporation", 20.50, 20.35)
    print("Stock Name:", S.getName())
    print("Stock Symbol:", S.getSymbol())
    print("The Previous Stock Price: $", S.getPreviousPrice())
    print("The Current Stock Price: $", S.getCurrentPrice())
    print("Change Percentage:", S.getChangePercent() + "%")
main()
