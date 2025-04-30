# Filename: Assignment 3- Distance Unit Conversion GUI Application  - Christian Powlette
# Date: 2023-12-1
# Christian Powlette
# Description: A program to convert from imperial to metric units or metric to imperial units, with the assistance of radio buttons
    # specfically, it converts kilometers to miles or miles to kilometers

# imports the tkinter library
from tkinter import *
# imports the tkinter tix library
from tkinter.tix import *
# Create the master window
window = Tk()
# sets default dimensions of the User Interface Window
window.geometry("500x210")
# Defines the title of the program as well as assignment for this assesment
window.title("Assignment 3 - Distance Unit Conversion GUI Application")

# DECLARATIONS

# Defines the Radio Buttons as String Variables "1" = km to miles, "2" = miles to km
convert_distance = StringVar()
# Defines Constant to convert Miles to Kilometers
MILES_TO_KILOMETERS = 1.609344
# Defines Constant to Kilometers to Miles
KILOMETERS_TO_MILES = 0.62137119

# Defines the function which is the process of obtaining the result of a select radio button, and converting from imperial to metric
    # or metric to imperial
def get_imperial_or_metric_results(_event = None):
    # Creates try and except for float numeric input only
    try:
        # Defines if statement that if "1", or radio button "Km to Mi" does the following
        if convert_distance.get() == "1": #Kilometers to Miles
            # gets input from in the entry box for converting kilometers to miles as a float input
            entry_distance_units_input = float(distance_units.get())
            # calculates the conversion from kilometer input to miles
            calculate_kilometers = entry_distance_units_input * KILOMETERS_TO_MILES
            # displays the results of the converted units
            label_distance_result_display.config(text="{:.2f}km converts to {:.2f}miles".format(entry_distance_units_input, calculate_kilometers))
        # Defines if statement that if "2", or radio button "Mi to Km" does the following
        elif convert_distance.get() == "2": # Miles to Kilometers
            # gets input from in the entry box  for converting miles to kilometers as a float input
            entry_distance_units_input = float(distance_units.get())
            # calculates the conversion from miles input to kilometers
            calculate_miles = entry_distance_units_input * MILES_TO_KILOMETERS
            # displays the results of the converted units
            label_distance_result_display.config(text= "{:.2f}mi converts to {:.2f}km".format(entry_distance_units_input, calculate_miles))
    # except non float input, and display error message
    except:
        # display error message for non float numeric input
        label_distance_result_display.config(text="ERROR: Float numeric input only")
# defines the function which is the process for clearing the entry boxes as well as labels
def clear_contents(_event = None):
    # sets the radio button as 1 by default
    convert_distance.set(1)
    # configures the label that displays the results of the converted distance units as empty or ("")
    label_distance_result_display.config(text="")
    # sets the distance units variable storing the input for the distance units to ""
    distance_units.set("")
#defines the function which is the process for the button that ends to program
def exit_program(_event = None):
    # utlizies a "quit()" to end the program
    quit()

# Adds tool tips
tooltip = Balloon(window)

# Row 0 Grid Widgets

# Creates the radio button for Kilometers to Miles
to_km_radio_button = Radiobutton(window, text='Kilometers to Miles', value=1, variable= convert_distance, command= get_imperial_or_metric_results)
# Defines the grid geometry to place the radio button in the window
to_km_radio_button.grid(row=0,column=0, padx= 5, pady = 5)
# Defines the tool tip binded to the radio button for Kilometers to Miles
tooltip.bind_widget(to_km_radio_button, msg= "Converts Kilometers to Miles")
# Creates the radio button for Miles to Kilometers
to_mi_radio_button = Radiobutton(window, text='Miles to Kilometers', value=2, variable= convert_distance, command= get_imperial_or_metric_results)
# Defines the grid geometry to place the radio button in the window
to_mi_radio_button.grid(row=0,column=3, padx= 5, pady = 5)
# Defines the tool tip binded to the radio button for Miles to Kilometers
tooltip.bind_widget(to_mi_radio_button, msg= "Converts Miles to Kilometers")
# Sets the Radio Buttons switched to toggled on kilometers by default
convert_distance.set(1)

# Row 1 Grid Widgets

# Defines the label "distance units prompt" which displays a prompt for users to enter input 
label_distance_units_prompt = Label(window, text="Enter Numeric Distance Units")
# Defines the grid geometery to place the label in the window
label_distance_units_prompt.grid(row=1, column =0, padx=5, pady= 5)
# Constructs "length" as a interger variable
distance_units = IntVar()
# Defines the entry "distance units" which accepts numeric input
entry_distance_units_input = Entry(window, textvariable=distance_units)
# Defines the grid geometry to place the entry box in the window
entry_distance_units_input.grid(row=1, column=1, padx=5, pady= 5)
# sets the entry box for the input of the distance units to direct the focus input to this widget (entry box)
entry_distance_units_input.focus()
#entry_distance_units_input = StringVar()
tooltip.bind_widget(entry_distance_units_input, msg= "Your numeric distance input goes here.")

# Row 2 Grid Widgets

# Defines the label prompt for the result of the convered distance units
label_distance_display = Label(window, text="Converted Distance") 
# Defines the grid geometry for  the label that displays the prompt for result of the converted distance units
label_distance_display.grid(row=2, column=0, padx=0, pady= 5)
# Defines the label for the result of the convered distance units
label_distance_result_display = Label(window, text="0") 
# Defines the grid geometry for the label that displays the result of the converted distance units
label_distance_result_display.grid(row=2, column=1, padx=0, pady= 5)
# Defines the tooltip for the label that displays results of the converted distance units
tooltip.bind_widget(label_distance_result_display, msg= "Result of your converted distance units shown here.")

# Row 3 Grid Widgets

# Defines the button that when pressed, converts the  units (kilometers to miles) or (miles to kilometers)
convert_button = Button(window, text="Convert", command=get_imperial_or_metric_results, height=3, width= 10) 
# Defines the grid geometry for the button that converts km to mi or vice versa
convert_button.grid(row=3, column = 0, columnspan =1)
# Defines the tooltip for the button that converts the distance units
tooltip.bind_widget(convert_button, msg= "This button, when pressed calculates unit conversion. Hotkey= <Return>")
# Defines the button that  when pressed, end the program 
exit_button = Button(window, text= "Exit", command = exit_program, padx = 5, pady =5, height= 2, width= 10)
# Defines the grid geometry for the button that ends the program
exit_button.grid(row = 3, column = 1, columnspan = 2, padx= 5, pady= 5)
# Defines the tooltip for the button that ends the program
tooltip.bind_widget(exit_button, msg= "This button, when pressed ends the program. Hotkey = <Alt-x>")
# Defines the button, that when pressed the reset the input entry and results label as well as sets the radio button to "km to mi" by default
reset_button = Button(window, text= "Reset", command= clear_contents, height= 3, width= 10) 
# Defines the grid geometry for the button
reset_button.grid(row=3, column = 3, columnspan= 2, padx = 5, pady= 5)
# Defines the tooltip for the button that resets the input entry and results label as well as sets the radio button to "km to mi" by default
tooltip.bind_widget(reset_button, msg= "This button, when pressed resets / clear the forum. Hotkey= <Alt-c> ")
# Defines the button to exit the program

# Hot Keys

# Defines the key to calculate / convert the metric to imperial units, or vice versa
window.bind("<Return>", get_imperial_or_metric_results)
# Defines the key combination "Alt key + c key" to "reset" / "clear contents"
window.bind("<Alt-c>", clear_contents)
# Defines the key combination "Alt key + x key" to exit / close the program
window.bind("<Alt-x>", exit_program)

# Creates the main loop for the user interface program
window.mainloop()