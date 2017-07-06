#From the File Employee, I will import the class Employee.
#
# Zachary Baltrus
# Homework 12

from Employee import Employee

# Below are 3 objects that contain all the info that you need for the employee
# I named the objects the first inital of their first and last name, along with the last 3 #'s of their ID
SM899 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
MJ119 = Employee("Mark Jones", 39119, "IT", "Programmer")
JR774 = Employee("Joy Rogers", 81772, "Manufacturing", "Engineer")

print("Name".ljust(20), "ID Number".ljust(20), "Department".ljust(20), "Position\n".ljust(20)) # To set the table
# When formatting the table, I found that using a fuction called ljust would be very easy and look the best.
# However, ljust doesnt work with ints so for the id number, I had to use format with padding on the end of the int.
print(SM899.name.ljust(20), "{:<20}".format(SM899.getIDNumber()), SM899.department.ljust(20), SM899.position.ljust(20))
print(MJ119.name.ljust(20), "{:<20}".format(MJ119.getIDNumber()), MJ119.department.ljust(20), MJ119.position.ljust(20))
print(JR774.name.ljust(20), "{:<20}".format(JR774.getIDNumber()), JR774.department.ljust(20), JR774.position.ljust(20))

