# Filename: Validation of User Input Assignment 1
# Date: 2023-09-22
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
# Description: A program to accpt user input and validation the input by using a series of particular if statements 
#   to ensure the ouput is valid.

# DECLARATIONS
# Constants
# Initialize student email

student_email = " Not Valid"
student_name = " Not Valid"
student_year_born = "Not Valid"
student_ethinicity = " Not Valid"

print()
print()
print()
print()
user_input = input("Please enter your student email ")

# Validate user input
# First Validation process - input must be a string
if str(user_input):
    # Second Validation process - input must have a "@" entered once
    if user_input.count("@") >= 2:
        print("ERROR student email must contain one @ symbol once")
    #Third Validation process - input must have the "@" symbol entered after a minimum of 2 characters
    elif user_input.find("@") <= 2:
        print("ERROR student email must have the @ symbol after a minimum of 2 characters")
    # Fourth Validation process - user input must end with .ca or .com
    elif user_input.endswith(".ca") or user_input.endswith(".com") == True:
        student_email = user_input
    
else:
    print("ERROR student email must contain characters and end with .com")

#OUTPUT
print("Your email address " + " is " + student_email)
print()
print()
print()

user_input = input("Please enter your name ")

# Validate user input
# First Validation process - input must be a string
if str(user_input):
    # Second Validation process - input must be longer than one letter
    if len(user_input) == 1:
        print("ERROR your name must be longer than 1 letter")
    # Third Valdiation process - input cannot contain numbers
    elif not user_input.isalpha():
        print("ERROR your name cannot contain numbers or special characters")
    else:
        student_name = user_input
else:
    print("ERROR student name must be a string")

#OUTPUT
print("Your name is " +  student_name)
print()
print()
print()

user_input = input("Please enter your age ")

# Validate user input
# First Validation process - input must be a integer, floats not accepted
if int(user_input):
    # Second Validation process - input must be lager than 120
    if len(user_input) >= 120:
        print("ERROR really? You're not truly that old!")
    # Third Validation process - input must cannot contain letters
    elif user_input.isalpha():
        print("ERROR your age cannot contain letters")
    else:
        student_name = user_input
else:
    print("ERROR your age must be a positive whole numbers")

#OUTPUT
print("You are " +  student_name + " years old")
print()
print()
print()

user_input = input("Please enter the year you were born ")

# Validate user input
# First Validation process - input must be a string
if int(user_input):
    # Second Validation process - input must be longer than one letter
    if len(user_input) <= 3:
        print("ERROR the year you were born must be longer than 3 digits (yyyy)")
    # Thirs Validation process - input must be a numeric value
    elif  user_input.isalpha():
        print("ERROR you must enter it in a numeric format")
    else:
        student_year_born = user_input
else:
    print("ERROR student name must be an integer")

#OUTPUT
print("You were born in " +  student_year_born)
print()
print()
print()

user_input = input("Please enter the your ethnicity ")

# Validate user input
# First Validation process - input must be a string
if str(user_input):
    # Second Validation process - input must be larger than 5 letters
    if len(user_input) > 5:
        print("ERROR your ethinicity must be larger than 5 letters)")
    # Third Validation process - input cannot contain numbers
    elif not user_input.isalpha():
        print("ERROR your race cannot contain numbers or specical characters")
    else:
        student_ethinicity = user_input
else:
    print("ERROR race must be characters only")

#OUTPUT
print("Your ethinicity is " + student_ethinicity)
print()
print()
print()

    
        

        

