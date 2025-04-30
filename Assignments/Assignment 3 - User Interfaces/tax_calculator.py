# tax_calculator.py
# Ken Hodgson
# 2023-11-23
#
# Description: App to calculate Ontario Sales tax

from tkinter import *
from tkinter.tix import *

# Declarations:
ONTARIO_TAX_RATE = 0.13

# Function definitions
# Declare event function `for calculate button.
def perform_calculation(_event = None):
    # Start a Try block.
    try:
        # Check if dollar amount entered is numeric. If it’s not, provide an error message.
        valid_dollar_amount = float(entry_dollar_amount.get())
        # Calculate the tax by multiplying valid_dollar_amount by ONTARIO_HST_RATE.
        tax_amount = valid_dollar_amount * ONTARIO_TAX_RATE
        # Output the tax amount in the “Calculated Tax” label as a dollar value, with 2 decimal places.
        label_tax_calculated_output.config(text = "${:.2f}".format(tax_amount))
    except:
        # Display error in label
        label_tax_calculated_output.config(text="ERROR: invalid input")

# Function to rest the form
def reset_form(_event = None):
    label_tax_calculated_output.config(text="")
    entry_dollar_amount.delete(0, END)
    entry_dollar_amount.focus()

# Create the master window
window = Tk()
window.title("Tax Calculator")
window.geometry("300x140")

# Add tool tips
tooltip = Balloon(window)

# Row 0 widgets
label_dollar_amount_prompt = Label(window, text="Enter the dollar amount:")
label_dollar_amount_prompt.grid(row=0, column=0, padx=5, pady=5)
entry_dollar_amount = Entry(window, width=15)
entry_dollar_amount.grid(row=0, column=1, padx=5, pady=5)
tooltip.bind_widget(entry_dollar_amount, msg="Enter the base amount before tax.")

# Row 1 widgets
label_tax_calculated_prompt = Label(window, text="Calculated tax:")
label_tax_calculated_prompt.grid(row=1, column=0, padx=5, pady=5)
label_tax_calculated_output = Label(window, border=2, relief=SUNKEN, width=12)
label_tax_calculated_output.grid(row=1, column=1, padx=5, pady=5)
tooltip.bind_widget(label_tax_calculated_output, msg="Calculated tax appears here.")

# Row 2 widgets
button_calculate = Button(window, text="Calculate", width=15, command=perform_calculation)
button_calculate.grid(row=2, column=0, padx=5, pady=5)
button_reset = Button(window, text="Reset", width=15, command=reset_form)
button_reset.grid(row=2, column=1, padx=5, pady=5)
tooltip.bind_widget(button_calculate, msg="Click to calculate the tax.")
tooltip.bind_widget(button_reset, msg="Click to reset everything.")

# Row 3 widgets
button_exit = Button(window, text="Exit", width=30, command=exit)
button_exit.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
tooltip.bind_widget(button_exit, msg="Click to end program.")

# Hot keys
window.bind("<Alt-c>", perform_calculation)
window.bind("<Alt-x>", exit)
window.bind("<Alt-r>", reset_form)
window.bind("<Return>", perform_calculation)

window.mainloop()
