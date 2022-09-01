import datetime
# Finding information about the current time including date
DateandTime = datetime.datetime.now()
print ("Current date and time is : ")
# printing data and time in particular format
print (DateandTime.strftime("%Y-%m-%d %H:%M:%S"))