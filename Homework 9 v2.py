# Flowchart & Programs v2
# This program will grab 20 random numbers and then it will
# print the smallest number, the largest number, the sum and
# the average of the numbers.
#
#
# Zachary Baltrus
# Homework 9
#
# CIS 1400

num = 0

import random

randomNumList = []

while num != 20:
    n = random.randint(0, 10000)
    randomNumList.append(n)
    print(n)
    num +=1

if num == 20:
    randomNumList.sort()
    sumOfNum = sum(randomNumList)
    avg = sumOfNum / num
    print ("The smallest number is ", randomNumList[0])
    print ("The largest number is", randomNumList[-1])
    print ("The sum of all the numbers is: ", sumOfNum)
    print ("The avgerage of all the numbers is ", avg)


