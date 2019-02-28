import datetime

x = datetime.datetime.now()

# Return the year and name of weekday.
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2018,10,5)
print(x)