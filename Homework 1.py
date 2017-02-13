#This program will display how many calories of cookies you eat
#Since the whole bag contains 30 cookies and all 30 cookies are 900 calories
#We will multiply the amount of cookies eaten by 900
#And then divide that number by 30
#
#
#Name: Zachary Baltrus
#Assignment: Homework 1
#
#CIT 1400

#This line of code will be an import for how many cookies are eaten
cookiesEaten = eval(input("How many cookies did you eat?: "))

#The next line of code will be calculating how many calories eaten
caloriesEaten = (cookiesEaten * 900)/30

#The final line of code will be displaying how many calories eaten
print("%.2f" % caloriesEaten, "calories")
                
