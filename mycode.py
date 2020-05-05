# Considering current time to be in 12 hour format
import datetime

# Function to convert the date format
def convertto24hrs(str1):

    

    # Checking if last two elements of time is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":

        return "00" + str1[2:-2]

        

    # remove the AM
    elif str1[-2:] == "AM":

        return str1[:-2]

    

    # Checking if last two elements of time is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":

        return str1[:-2]

        

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

now = datetime.datetime.now()

print ("Current time : ")

print (now.strftime("%I:%M:%S%p"))

str=now.strftime("%I:%M:%S%p")

print(convertto24hrs(str))

print ("Current date and time : ")

print (now.strftime("%Y-%m-%d %H:%M:%S"))


