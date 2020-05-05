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
