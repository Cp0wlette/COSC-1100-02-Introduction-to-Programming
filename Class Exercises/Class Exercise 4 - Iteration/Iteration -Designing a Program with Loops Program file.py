# Filename: Assignment #3
# Date: 2023-09-22
# Christian Powlette
#   Referenced from K. Hodgson https://durhamcollege.desire2learn.com/d2l/le/content/502256/viewContent/7003921/View
# Description: A program to

# DECLARATIONS
order = 0
traditional_hot_dogs = 0
veggie_hot_dogs = 0
curry_hot_dogs = 0
total_sold = 0
traditional_hot_dogs_percent = 0
veggie_hot_dogs_percent = 0
curry_hot_dogs_percent = 0
# Constants

for i in range(0, 3, 1):
    print("")
    print("")
    print("What kind of hot dogs were sold?")
    print("1. Traditional hot dogs")
    print("2. Veggie hot dogs")
    print("3. Curry hot dogs")
    print("")
    order = input("Select a number from 1-3 or '4': ")
    if order.isalpha():
        print("Error! Invalid input, the options are 1, 2, 3, and 4.")
    elif order == 1:
        print("")
        print("")
        if order.isalpha():
            print("Error! Invalid input, the options are 1, 2, 3, and 4.")
        traditional_hot_dogs = input("How many traditional hot dogs were sold? ")
        print("")
        i += 1
    elif order == 2:
        print("")
        print("")
        if order.isalpha():
            print("Error! Invalid input, the options are 1, 2, 3, and 4.")
        veggie_hot_dogs = input("How many veggie hot dogs were sold? ")
        print("")
        i += 1
    elif order == 3:
        print("")
        print("")
        if order.isalpha():
            print("Error! Invalid input, the options are 1, 2, 3, and 4.")
        curry_hot_dogs = input("How many curry hot dogs were sold? ")
        print("")
        i += 1
    elif order == 4:
        i +=  4
        print("---------------------------------------------")
        total_sold = traditional_hot_dogs + veggie_hot_dogs + curry_hot_dogs
        print("The amount of Traditional hot dogs sold was", + traditional_hot_dogs)
        print("The amount of Veggie hot dogs sold was", + veggie_hot_dogs)
        print("The amount of Curry hot dogs sold was", + curry_hot_dogs)
        print("---------------------------------------------")
        break
    else:
        print("Error! Invalid input, the options are 1, 2, 3, and 4.")

#Process
if traditional_hot_dogs and veggie_hot_dogs and curry_hot_dogs == 0:
    print("Error! no hot dogs were selected")

else:
    print("---------------------------------------------")
    total_sold = traditional_hot_dogs + veggie_hot_dogs + curry_hot_dogs
    if total_sold == 0:
        print("Error! no hot dogs were selected")
    else:
        traditional_hot_dogs_percent = traditional_hot_dogs / total_sold
        traditional_hot_dogs_percent = traditional_hot_dogs_percent * 100

        veggie_hot_dogs_percent = veggie_hot_dogs / total_sold
        veggie_hot_dogs_percent = veggie_hot_dogs_percent * 100

        curry_hot_dogs_percent = curry_hot_dogs / total_sold
        curry_hot_dogs_percent = curry_hot_dogs_percent * 100

        #Output
        print(str(traditional_hot_dogs) + " traditional hot dogs were sold")
        print(str(veggie_hot_dogs) + " veggie hot dogs were sold")
        print(str(curry_hot_dogs) + " curry hot dogs were sold")
        print("---------------------------------------------")
        print(str(traditional_hot_dogs_percent) + "%" + " of traditional hot dogs were sold")
        print(str(veggie_hot_dogs_percent) + "%" + " of veggie hot dogs were sold")
        print(str(curry_hot_dogs_percent) + "%" + " of curry hot dogs were sold")
        print("---------------------------------------------")
        print(str(total_sold) + " were sold in total")
        print("---------------------------------------------")