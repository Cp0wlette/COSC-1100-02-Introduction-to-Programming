# Filename: Validation of User Input Assignment
# Date: 2023-09-22
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
# Description: A program to accpt user input and validation the input by using a series of particular if statements 
#   to ensure the ouput is valid.

# DECLARATIONS
# Initialize student email
student_email = "Not Valid"

# Constants



user_input = input("Please enter your student email")

# Validate user input
# First Validation process - input must be a string
if str(user_input):
    # Second Validation process - input must have a "@" entered once
    if user_input.string.count(@) > 1:
        print("ERROR student email must contain one @ symbol once")
    #Third Validation process - input must have the "@" symbol entered after a minimum of 2 characters
    elif user_input.string.find(@) <= 2:
        print("ERROR student email must have the @ symbol after a minimum of 2 characters")
    elif user_input.string.endswith(.com) == False:
        print("ERROR student email must end with .com")
else:
    print("ERROR student email must contain characters")

#OUTPUT

print("Well done, your email, " + user_input + " is valid")
    
        

        

