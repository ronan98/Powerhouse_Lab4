# Powerhouse | CSE408 Spring 2020 Lab 4 Version Control System GitHub-advanced
# Created by: Ronan Panopio, Heidy Ramirez, Abdullah Alharthi, Faisal Alsaif, Justin Ciccone

# Ronan Panopio | Reverse User Inputted String

def reverseString(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print("Your reversed string is: ", reversed_string)

stringInput = input("Enter a string you want reversed: ")
print("\n\nYou have entered the string: ", stringInput)
reverseString(stringInput)

#Justin Ciccone Part B
number = int(input("enter any number"))

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
            
else:
    print(number, "is not a prime number")

#Abdullah alharthi

F = int(input("Enter how many numbers to output of the fibonacci series:\n"))

One = 0

Two = 1


for i in range(F):

    print(One)

    store = One

    One = Two

    Two = store+Two


#Heidy Part E

import re   # This module provides regular expression matching operations

def check_password(x):    #Function that checks the validity of the password
    y = True #condition to check the logic
    while y:
        if(len(x)<6):   #password can't be less than 7 characters
            break
        elif not re.search("[a-z]",x):  #break if the password does not contain a-z
            break
        elif not re.search("[0-8]",x):  #break if the password does not contain 0-8
            break
        elif not re.search("[!@#$%^&*?]",x): #break if the password does not contain these
            break
        else:
            print("Valid")  #if the above fail then it's valid
            y=False
            break
    if y:
        print("Invalid")  #true statement

new_password = input("Create a new password ")
check_password(new_password)

#Faisal | convert time to 24 hours 
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


