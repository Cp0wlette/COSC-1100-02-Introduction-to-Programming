# Filename: Pizza Pi Iteration - Assignment 1 - Christian Powlette
# Date: 2023-10-20
# Christian Powlette
#   Referenced from K. Hodgson Intro to programming template
# Description: A program to prompt a user to enter a diameter of a pizza in inches and display a variety of pizza slice configurations.


# DECLARATIONS

#import math library
import math

#Variables
#Stores the area of the pizza
pizza_area = 0
#stores the diameter of the pizza
pizza_diameter = 1
#stores the calculatation for 6 slices
six_slices = 0
#stores the calculatation for 8 slices
eight_slices = 0
#stores the calculatation for 10 slices
ten_slices = 0
#stores the calculatation for 12 slices
twelve_slices = 0
#stores the calculatation for 16 slices
sixteen_slices = 0


# This while loop will continue to loop and repeat until the user input is equal to 0
while pizza_diameter != 0:
    #Print space line
    print("")
    # Display prompt for user to input a value for pizza diameter
    pizza_diameter = input("Please enter the diameter of your pizza (0 to end the program) ")
    #Print space line
    print("")
    # Try to convert input into float, and if it cannot print an Error Message
    try:
        pizza_diameter = float(pizza_diameter)
    except ValueError:
        print("ERROR enter a numeric value")
        continue
    # IF the input for the pizza diamter is greater than or equal to 8 or less than or equal to 24 do the following
    if pizza_diameter >= 8 and pizza_diameter <= 24:
        # Calculate the area of the pizza by utlizing the area of a circle formula by diving the diameter by 2 and mutliplying both to obtain the radius 
        # to the power of 2
        pizza_area = math.pi * ((pizza_diameter/2)*(pizza_diameter/2))
            # If the diameter of the pizza chosen is less than or equal to 8 or less than or equal to 12 then display the pizza diameter in 6 slices
        if pizza_diameter >= 8 or pizza_diameter >= 24:
            #store the pizza area in a variable after diving it by 6
            six_slices = pizza_area / 6
            # store the rounded number from the previous calculation
            six_slices =  round(six_slices, 2)
            #print the output message of pizza results with calculation and units.
            print("The pizza cut into 6 slices results in " + str(six_slices) + " inches per slice")

        # If the diameter of the pizza chosen is less than or equal to 12 or less than or equal to 14 then display the pizza diameter in 6 or 8 slices
        if pizza_diameter >= 12 or pizza_diameter >= 24:
            #store the pizza area in a variable after diving it by 8
            eight_slices = pizza_area / 8
            # store the rounded number from the previous calculation
            eight_slices =  round(eight_slices, 2)
            #print the output message of pizza results with calculation and units.
            print("The pizza cut into 8 slices results in " + str(eight_slices) + " inches per slice")

        # If the diameter of the pizza chosen is less than or equal to 14 or less than or equal to 16 then display the pizza diameter in 6, 8, or 10 slices
        if pizza_diameter >= 14 or pizza_diameter >= 24:
            #store the pizza area in a variable after diving it by 10
            ten_slices = pizza_area / 10
            # store the rounded number from the previous calculation
            ten_slices =  round(ten_slices, 2)
            #print the output message of pizza results with calculation and units.
            print("The pizza cut into 10 slices results in " + str(ten_slices) + " inches per slice")

        # If the diameter of the pizza chosen is less than or equal to 16 or less than or equal to 20 then display the pizza diameter in 6, 8, 10, 12, or 12 slices.
        if pizza_diameter >= 16 or pizza_diameter >= 24:
            #store the pizza area in a variable after diving it by 12
            twelve_slices = pizza_area / 12
            # store the rounded number from the previous calculation
            twelve_slices =  round(twelve_slices, 2)
            #print the output message of pizza results with calculation and units.
            print("The pizza cut into 12 slices results in " + str(twelve_slices) + " inches per slice")

        # If the diameter of the pizza chosen is less than or equal to 20 or less than or equal to 24 then display the pizza diameter in 6, 8, 10, 12 or 16 slices
        if pizza_diameter >= 20 or pizza_diameter >= 24:
            #store the pizza area in a variable after diving it by 16
            sixteen_slices = pizza_area / 16
            # store the rounded number from the previous calculation
            sixteen_slices =  round(sixteen_slices, 2)
            #print the output message of pizza results with calculation and units.
            print("The pizza cut into 16 slices results in " + str(sixteen_slices) + " inches per slice")
    # Else, if the user enters a 0 the program will end
    else:
        # If the pizza diameter does not equal 0 despite these checks, it will reiterate that it must be within the range of 8 and 24 inches
        if pizza_diameter != 0:
            print("Error! --must be between 8 and 24 inches.")