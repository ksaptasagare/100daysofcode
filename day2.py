#making an age calculator

#importing system library to get the current/live date and time
#importing datetime module for now()
import datetime

#making an age calculator class
class agecalc:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
    
    #method to calculate the age in years
    def age_y(self):
        super()
        # using now() to get current time
        today = datetime.datetime.now().date()
        #converting user input to date format
        dob = datetime.date(self.y, self.m, self.d)
        age = int((today-dob).days/365.25)
        return age

#getting the date from the user         
print("Enter a date.")
y = int(input("Year: "))
m = int(input("Month: "))
d = int(input("Day: "))

#creating an object of class and calling the method
obj = agecalc(d,m,y)
age = obj.age_y()
print("The date of birth is {0:0}-{1:0}-{2:2}".format(d,m,y))
print("The age is {0:3}".format(age))