""" A date is not a datatype in python, but we can import a module
name datetime to work with dates as date objects"""

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)

print (x.strftime("%A"))

x = datetime.datetime(2018, 11, 2)
print(x)

x = datetime.datetime(2018, 11, 2)
print(x.strftime("%B"))

