# Filename: Class Exercise - User Interfaces - Christian Powlette
# Date: 2023-11-24
# Christian Powlette
# Description: 

#DECLARATIONS

from tkinter import *
from tkinter.tix import *
window = Tk()

window.geometry("300x200")
window.minisize(screenwidth = 250,screenheight = 150)

def getArea(Width,Height):
    return Width * Height

def clickArea():
    area.set(getArea(height.get(), width.get()))


window.title("Class Exercise - User Interfaces Calculate Area Program")

#Row 0 widgets
Label(window, text="Width").grid(row=0, column =0)
width = IntVar()

Entry(window, textvariable=width).grid(row=0, column=1)
Label(window, text="Height") .grid(row=1, column=0)
height = IntVar()

#Row 1 widgets
Entry(window, textvariable=height) .grid(row=1, column=1)
Label(window, text="Area") .grid(row=2, column=0)
area=IntVar()

#Row 2 widgets
Label(window, textvariable=area) .grid(row=2, column=1)
button = Button(window, text="Calculate Area", command=clickArea)

#Row 3 widget
button.grid(row=3, column=0, columnspan=2)

window.mainloop()
