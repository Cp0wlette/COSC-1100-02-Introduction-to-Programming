# Filename: Validation of User Input Assignment 2
# Date: 2023-09-22
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
# Description: A program to accpt user input and validation the input by using a series of particular if statements 
#   to ensure the ouput is valid.

# DECLARATIONS
# Initialize student email
student_name = " Not Valid"
# Constants



user_input = input("Please enter your name (Elon Musk's children are welcome) ")

# Validate user input
# First Validation process - input must be a string
if str(user_input):
    # Second Validation process - input must be longer than one letter
    if len(user_input) == 1:
        print("ERROR your name must be longer than 1 letter")
    elif user_input.isalnum() or user_input.isalpha():
        print("ERROR your name cannot contain numbers or special characters")
    else:
        student_name = user_input
else:
    print("ERROR student name must be in letters")

#OUTPUT
print()
print("Your name is " +  student_name)