# StudentIDValidation.py
# K. Hodgson
# 2023-09-28
#
# Description: Program to accept and validate a student ID at Durham College.

# Declarations:
# Initialize student ID variable:
student_id = "Not Valid"

# Input
# Prompt the user to enter their student number
user_input = input("Please enter your student ID #: ")

# Process
# Validate the user input
# 1 - Must be numeric only
if user_input.isnumeric():
    # 2 - Numeric data entered--check to see if 9 digits have been entered
    if len(user_input) == 9:
        # Valid student number entered. Store it in the output variable.
        student_id = user_input
    else:
        # Was not exactly 9 digits--show an error message.
        print("ERROR: \nStudent ID must be 9 digits.")
else:
    # Non-numeric entry--show an error message:
    print("ERROR: \nStudent ID must be numeric.")

# Output
# Show the validated results:
print("\nRESULTS:")
print("Student ID#:", student_id)
print()

# End program:
input("Press <Enter> to end program...")
