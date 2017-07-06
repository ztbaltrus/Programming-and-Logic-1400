# Python File IO: Ticket Prices
# The focus on this program is to open a file with ticket prices
# and then to calculate the prices and print them out onto another file
# called output
#
# Zachary Baltrus
# CIS 1400
#
# Homework 10

# Importing os.path to make it easier for the program to find the file
import os.path

# Defining the list for ticket prices
ticketPriceList = []

# Opening both files
ticketPrices = open(os.path.expanduser("~/Desktop/ticket.txt"), "r")
output = open(os.path.expanduser("~/Desktop/output.txt"), "w")

# the program will read ticket.txt line by line until there is a blank space
line = ticketPrices.readline()
while line != '':
    splitLine = line.split()
    ticketPriceList.append(splitLine[1]) # We only want the ticket prices and not the seat number
    line = ticketPrices.readline() 
    

amountInList = len(ticketPriceList) # Will count how many items are in the list
listSum = sum(map(float, ticketPriceList)) # Will grab the sum on the list
avgTicketPrice = listSum / amountInList # Will divide the sum by how many in the list to get the average.

ticketPriceList.sort() # Will sort the ticket prices by smallest to largest
maxTicketPrice = ticketPriceList[0] # Will grab the first in the list
minTicketPrice = ticketPriceList[-1] # Will grab the last in the list

# Writing all of these lines to output.txt
output.write("*******************************************\n\t\tTICKET REPORT\n*******************************************\n")
output.write("\nThere are {} tickets in the database \n".format(amountInList))
output.write("\nMaximum Ticket price is ${}\n".format(maxTicketPrice))
output.write("Minimum Ticket price is ${}\n".format(minTicketPrice))
output.write("Average Ticket price is ${}\n".format(avgTicketPrice))
output.write("\nThank you for using our ticket system!\n\n*******************************************")

# Closing all of the files
ticketPrices.close()
output.close()
