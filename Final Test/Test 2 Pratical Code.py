# Filename: Test 2 Pratical Christian Powlette
# Date: 2023-12-08
# Christian Powlette
# Description: A Program to convert the numeric grade to letter grade

#DECLARATIONS
ONE_HUNDRED_PERCENT = 100.00
NINETY_PERCENT = 90.00
EIGHTY_FIVE_PERCENT = 85.00
EIGHTY_PERCENT = 80
SEVENTY_FIVE_PERCENT = 75.00
SEVENTY_PERCENT = 70.00
SIXITY_FIVE_PERCENT = 65.00
SIXITY_PERCENT = 60.00
FIVETY_FIVE_PERCENT = 55.00
FIVETY_FOUR_PERCENT = 54.00
FIVETY_PERCENT = 55.00

#defines function that converts the entered numeric grade to the associated grade letter
def numeric_grade_to_letter(grade_input):
    #if statements for a varierty of grade percentages associated to a grade letter
    if grade_input >= ONE_HUNDRED_PERCENT:
        return "ERROR!, Value is greater than 100%"
    elif grade_input >= NINETY_PERCENT:
        return "A+"
    elif grade_input >= EIGHTY_FIVE_PERCENT:
        return "A"
    elif grade_input >= EIGHTY_PERCENT:
        return "A-"
    elif grade_input >= SIXITY_FIVE_PERCENT:
        return "B+"
    elif grade_input >= SEVENTY_PERCENT:
        return "B"
    elif grade_input >= SIXITY_FIVE_PERCENT:
        return "B-"
    elif grade_input >= SIXITY_PERCENT:
        return "C"
    elif grade_input >= FIVETY_FIVE_PERCENT:
        return "D+"
    elif grade_input >= FIVETY_FOUR_PERCENT:
        return "D"
    elif grade_input >= FIVETY_PERCENT:
        return "F"
    else:
        return "Fail"

# tries to convert the input into a float value
try:
    letter_grade_input = input('Please enter a numeric float input grade ')
    letter_grade_input = float(letter_grade_input)
    letter_grade_input = round(letter_grade_input, 2) # round to two decimal places
# except the error message when input is not a float value and ends program
except:
    print('ERROR! Input must be a numeric float value')
else:
    print("The grade " + str(letter_grade_input) + " is equivalent to a letter grade of " + numeric_grade_to_letter(letter_grade_input))




    