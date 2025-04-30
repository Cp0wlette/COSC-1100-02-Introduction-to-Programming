# Filename: Assingment #1 - IceCream Problem 
# Date: 2023-09-15
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
# Description: A program to convert the inputs of the number of each size of 
#	   ice cream cones sold in a week to the total quantity of ice cream sold.

# DECLARATIONS

# Constants
# Constant for each unit of measure

# Constant for the volume of kiddie cones 60 mL
KIDDIE_CONES = 60
# Constant for the volume of small cone 120 mL
SMALL_CONES = 120
# Constant for the volume of medium cone 240 ml
MEDIUM_CONES = 240
# Constant for the volume of large cone 360 mL
LARGE_CONES = 360

# Variables
# Variable to hold the result—total weekly volume in mL
weekly_volume = 0

# print greeting
#   "Hello Stranger!"
print("Hello Stranger")
print("")

# INPUT
#print prompt
#   press "ENTER" to continue
input("Press Enter to countinue ")
print("")
#<user presses "ENTER">


# Prompt the user to enter input for each amount of ice cones sold in one week i.e., 
print("Please enter the number of ice cream sold for various cones:")
print("")
# prompt user to enter Kiddie cones (1/2 scoop) sold, then convert stored value into a float. 
kiddie_cones_sold = int(input("Please enter number of (1/2 scoop) kiddie cones sold this week "))

# small cones (1 scoop), then convert stored value into a float.
small_cones_sold = int(input("Please enter number of (1 scoop) small cones sold this week "))

# Medium cones (2 scoops), then convert stored value into a float.
medium_cones_sold = int(input("Please enter number of (2 scoops) medium cones sold this week "))

# Large cones (3 scoops). then convert stored value into a float.
large_cones_sold = int(input("Please enter number of (3 scoops) large cones sold this week "))
 
# PROCESSING
# For each Stored ice cream cone variable, multiply it's respective ice cream consant. 
# kiddie cones (Half a scoop) multiplied by constant,
kiddie_cones_sold = kiddie_cones_sold * KIDDIE_CONES
# One scoop  multiplied by constant, 
small_cones_sold = small_cones_sold * SMALL_CONES
#  2 scoops = 240 multiplied by constant. 
medium_cones_sold = medium_cones_sold * MEDIUM_CONES
#  3 scoops = 360 multiplied by constant
large_cones_sold = large_cones_sold * LARGE_CONES
# Add all variables together and store the amount in variable.
weekly_volume = (kiddie_cones_sold + small_cones_sold + medium_cones_sold + large_cones_sold)

# OUTPUT
# Display The total amount of each ice cream sold in one week with variable and "milliliters" placed at the end of output.

print ("The total amount of ice cream sold in one week is: ", str(weekly_volume) + " ml")