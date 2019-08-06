import datetime
import calendar

# creating one variable called x
x = datetime.datetime.now()

print(x)
print(x.year)
# month
print(x.strftime("%B"))
# Day
print(x.strftime("%A"))
# Date
print(x.strftime("%C"))

# perticular date to print
y = datetime.datetime(2020, 8, 19)
print(y)

# particular calender to print
cal = calendar.month(2017, 2)
print(cal)

