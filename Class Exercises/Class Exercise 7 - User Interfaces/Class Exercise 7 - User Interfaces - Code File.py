# Filename: Class Exercise - User Interfaces - Christian Powlette
# Date: 2023-11-24
# Christian Powlette
# Description: A Program to calculate and output the length of width of a rectangle, 
#               where the length and width is obtained from the user's input as well

from tkinter import *
from tkinter.tix import *
# Create the master window
window = Tk()
# sets default dimensions of the User Interface Window
window.geometry("350x180")
# Defines the title of the program as well as exercsie for this assignment
window.title("Class Exercise 7 - User Interfaces: Calculate Rectangle Area Program")
#DECLARATIONS

#defines the function which is the process of obtaining Area from the user's input after entering length and width of a rectangle.
def calculate_results(_event = None):
    try:
        # Stores the length the function to obtain the length in the variable
        rectangle_length = float(length.get())
        # Stores the length the function to obtain the width in the variable
        rectangle_width = float(width.get())
        # If entries convert to float values okay, we can calculate the area and perimeter
        rectangle_area = rectangle_length * rectangle_width
        rectangle_perimeter = 2 * rectangle_length + 2 * rectangle_width
        # Display the results in the label area
        label_area_result_display.config(text="{:.2f} m".format(rectangle_area))
        # Display the results in the label perimeter
        label_perimeter_result_display.config(text="{:.2f} m".format(rectangle_perimeter))
    except:
        # User has entered a value that cannot be converted to float
        label_area_result_display.config(text="Error: Please enter only numbers.")
        label_area_result_display.config(text="Error: Please enter only numbers.")
# Defines the function which is the process fro the button that resets/ clears the entry boxes for length and width
def clear_contents(_event = None):
    length.set("")
    width.set("")
    label_area_result_display.config(text="")
    label_perimeter_result_display.config(text="")
#defines the function which is the process for the button that ends to program
def exit_program(_event = None):
    quit()

# Row 0 Grid Widgets

# Defines the label "length" and it's properties (it's grid), 
# as well as the variable that stores length of the rectangle entered from user input
label_length_prompt = Label(window, text="Enter length").grid(row=0, column =0, padx=5, pady= 5)
# Constructs "length" as a interger variable
length = IntVar()
#Defines the entry for the length and it's properties (it's grid)
entry_length_user_input = Entry(window)
entry_length_user_input = Entry(window, textvariable=length).grid(row=0, column=1, padx=5, pady= 5)
entry_length_user_input = StringVar()

# Row 1 Grid Widgets

# Defines the label "width" and it's properties (it's grid), 
# as well as the variable that stores width of the rectangle entered from user input
label_width_prompt = Label(window, text="Enter width") .grid(row=1, column=0, padx=5, pady= 5)
# Contructs "width" as a interger variable
width = IntVar()
#Defines the entry to obtain user input for the width and it's properties (it's grid)
entry_width_user_input = Entry(window)
entry_width_user_input = Entry(window, textvariable=width) .grid(row=1, column=1, padx=5, pady= 5)
entry_width_user_input = StringVar()

#Row 2 Grid Widgets

# Defines the label and it's properties (it's grid), that displays the text "Area"
label_area_display = Label(window, text="Area") .grid(row=2, column=0, padx=0, pady= 5)
# Contructs "area" as a interger variable
area = IntVar()
# Defines the label and it's properties (it's grid),  that displays the calculation of area
label_area_result_display = Label(window, text="0") 
label_area_result_display.grid(row=2, column=1, padx=0, pady= 5)
# Defines the button Grid for the button "Calculate Area", used to calculate the area of the length and width variables

# Row 3 Grid Widgets

# Defines the label "perimeter" and it's properties (it's grid), that displays the text "Perimeter"
label_perimeter_display = Label(window, text="Perimeter") .grid(row=3, column=0, padx=0, pady= 5)
# Contructs "perimeter" as a interger variable
perimeter = IntVar()
# Defines the label "perimeter" and it's properties (it's grid), that displays the calculation of perimeter
label_perimeter_result_display = Label(window, text="0")
label_perimeter_result_display.grid(row=3, column=1, padx=5, pady= 5)
# Defines the button Grid for the button "Calculate Perimeter", used to calculate the area of the length and width variables
calculate_results_button = Button(window, text="Calculate", command=calculate_results, padx=5, pady= 5) 
calculate_results_button.grid(row=4, column = 0, columnspan =1, padx=5, pady= 5)
# Defines the button Grid for the reset button "Reset", used to reset the entry box that accepts input from the user


#Row 4 Grid Widgets

calculate_results_button.grid(row=4, column = 0, columnspan =1, padx=5, pady= 5)
# Defines the button the reset the entries
Reset_button = Button(window, text= "Reset", command= clear_contents, padx= 5, pady= 5) .grid(row=4, column = 1, columnspan= 2, padx = 5, pady= 5)
# Defines the button to exit the program
Exit_button = Button(window, text= "Exit", command = exit_program, padx = 5, pady =5) .grid(row = 4, column = 2, columnspan = 5, padx= 5, pady= 5)

#Hot Keys
# Defines the key to calculate results
window.bind("<Return>", calculate_results)
# Defines the key to "reset" / "clear contents"
window.bind("<Delete>", clear_contents)
# Defines the key to exit / close the program
window.bind("<Escape>", exit_program)


# Creates the main loop for the user interface program
window.mainloop()
