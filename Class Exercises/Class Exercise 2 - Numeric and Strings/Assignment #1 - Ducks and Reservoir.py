# Filename: Assignment #1 - Ducks and reservoir Problem 
# Date: 2023-09-22
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
#   Referenced from Amazon (dimensions of the rubber ducks) https://www.amazon.ca/Halloween-Assorted-Supplies-Birthday-Decorations/dp/B0C9LYBVKD/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.fff4d389-5f12-4a3d-bbdb-de5278b37977%3Aamzn1.sym.fff4d389-5f12-4a3d-bbdb-de5278b37977&cv_ct_cx=rubber+ducks&keywords=rubber+ducks&pd_rd_i=B0C9LYBVKD&pd_rd_r=817c06bc-c888-456b-b733-6dd2a9d69d73&pd_rd_w=2rsdT&pd_rd_wg=2K3SH&pf_rd_p=fff4d389-5f12-4a3d-bbdb-de5278b37977&pf_rd_r=HBQWJPXHNXT4XHNQHQC1&qid=1695322510&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-2-acb80629-ce74-4cc5-9423-11e8801573fb-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&psc=1
# Description: A program to calculate the number of ducks that can fill a estimated 
#       length and width to calculate area of the Durham College's reservoirs

# DECLARATIONS

# Constants
# The dimensions of the rubber ducks in centimeters
RUBBER_DUCKS_LENGTH = 7.62
RUBBER_DUCKS_WIDTH = 6.35 


# print greeting
#   "Hello Stranger!"
print("")
print("")
print("Hello Stranger")
print("")

# INPUT
#print prompt press "ENTER" to continue
input("Press Enter to countinue ")
print("")
print("")
print("")
print("")
#<user presses "ENTER">

# Prompts user to enter to enter the dimensions of the reservoirs;
print("Please enter the following dimensions for the reservoirs: ")
print("")
print("")
# prompt user to enter the length of the reservoir 
reservoir_length = float(input("Please enter a estimated numerical value for length in meters of the reservoir: "))
print("")                         

#<user enters length estimate>

# prompts user to enter the width of the reservoir
reservoir_width = float(input("Please enter a estimate numerical value for width in meters of the reservoir: "))
print("")

#<user enters width estimate>

# PROCESSING
# convert the dimensions of the reservoir by mutliplying each variable by 100;

# convert the length of the reservoir by mutlipying by 100
reservoir_length = reservoir_length * 100
# convert the width of the reservoir by mutlipying by 100
reservoir_width = reservoir_width * 100
# mutliply together the reservoir dimensions variables, to get the area of the reservoir
reservoir_area = reservoir_length * reservoir_width

# mutliply together the rubebr ducks dimensions variables, to get the area of the rubber ducks
rubber_duck_area = RUBBER_DUCKS_LENGTH * RUBBER_DUCKS_WIDTH

number_of_rubber_ducks_to_fill = reservoir_area / rubber_duck_area
# OUTPUT
# Display the calculated result variable to the user with a formatted string
print(str(number_of_rubber_ducks_to_fill) + " ducks can fit inside the Durham College reservoirs")
# Pause to let the user view the result.
input("")