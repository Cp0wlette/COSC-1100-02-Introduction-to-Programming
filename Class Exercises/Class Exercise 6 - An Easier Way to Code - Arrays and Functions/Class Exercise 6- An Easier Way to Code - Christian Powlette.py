# Filename: Class Exercise 5- Learning to Use Arrays Effectively - Christian Powlette
# Date: 2023-11-3
# Christian Powlette
# Description: A program to prompt a user to enter a their marks for a varierty of assesments to calculte their current mid-term mark.

# DECLARATIONS
#  Define function get_average_input, this function gets the input from the user
# First paramter will accept the type of assignment which will be a list variable
# Second paramter will accept the weight type for the assignment which will be a interger
# Third parameter will accept the iteration amount to loop that amount of times input will be collected, which will be a integer
# Fourth paramter is the assignment_text, which will print out the instructions for the specfic  type of input collected, which will be a string
def get_average_input(assignment_type: list = [], weight_type: int = 0, iteration_amount: int = 0, assignment_text: str = "Default"):
    while True:
        #loops according to the iteration amount entered in function
        for i in range(iteration_amount):
            #prints instructions for the user
            print("Please enter your numeric integer mark for the", assignment_text, "assesment")
            #obtains input from user and stores in variable
            # tries to convert input into intger for validation
            while True: 
                try:
                    average_input = int(input())
                    break
                    # if it cannot turn into a integer print the following ERROR message
                except ValueError:
                    # prints the ERROR message
                    print("ERROR enter a numeric value")
            # appends the input which is multiplied by the weight type first
            assignment_type.append(average_input * weight_type)
        return assignment_type
        break

# Define function caculate_weighted_average, this function does some calulations of the input
# First paramter will accept the type of input which will be a list variable
# Second paramter will accept the type of weight which will be a integer
# Third paramter will accept total weights for the type of assignment
# Foruth paramter  will accept the iteration amount to loop that amount of times a variable will be ccalculated
def calculate_weighted_average(assignment_type: list = [], weight_type: int = 0, total_weights_type: int = 0, iteration_amount: int = 0):
    # turns in local variable into a global variable
    global total_weights
    for i in range(iteration_amount):
        # calculate the sum from each mark element in the list
        assignment_sum_type = sum(assignment_type)
        # add the weights to the total weight to get total
        total_weights_type += weight_type
    # return the sum of the type of assignment list entered first then returns the sum of the total weights of the type of weight of the assignment secondly
    return assignment_sum_type, total_weights_type
    
#Constants
#Variables

#Variable for final output weighted average mark
total_mark = 0


# pre class activities total weight variable
pre_class_total_weights = 0
# class exercise total weight variable
class_total_weights = 0
#assignment total weight variable
assignment_total_weights = 0
#test total weight variable
test_total_weights = 0

#Variables for each assesment list containing each mark obtained by the user's input variable
pre_class_activities = [0]
class_exercises = [0]
assignments = [0]
test = [0]

#Variable determing the running  status of the while loop
session = 1
# While session does not equal 0 do the following
while session != 0:
    #Print space line
    print("")
    #print intructions for user
    print("Please enter your mark for the various assesments ")
    #Print space line
    print("")
    #Function get_average_input
    # First parameter is the type of assignment which will be used in the function to append the marks inputed into the list
    # Second pararameter is the weight type for the type of assignment chosen in the first parameter
    # Third parameter is the iteration amount, how much which determines how many inputs it will prompt the user to obtain for one assignment
    # Foruth paramter is the string to insert for the type of assignment that will explain what assignment to enter input for
    get_average_input(pre_class_activities, 3, 5, "pre class activity")
    get_average_input(class_exercises, 3, 4, "class exercise")
    get_average_input(assignments, 10, 1, "assignment")
    get_average_input(test, 6, 2, "test")
    # once done / checking the following break and get out of loop
    break

#Function calculate_weighted_average
# First parameter is the type of assignment which will be used to calculate
# Second paramter is the weight type that will be looped in accordance to the fourth paramter to get the total weight for all assignmnets
# Third parameter is the total weight in accordance to the amount of times it will be looped in the fourth paramter 
# Fourth paramter is the  total weight for the assignment
# Fifth parameter is the iteration amount, how much which determines how many inputs it will prompt the user to obtain for one assignment

# Returned value from calculate weighted average obtains the sum of type of assesment and the total weight of the assesment
pre_class_sum, pre_class_total_weights = calculate_weighted_average(pre_class_activities, 3, pre_class_total_weights, 5)
class_exercise_sum, class_total_weights  = calculate_weighted_average(class_exercises, 3, class_total_weights, 4)
assignment_sum, assignment_total_weights = calculate_weighted_average(assignments, 10, assignment_total_weights, 1)
test_sum, test_total_weights = calculate_weighted_average(test, 6, test_total_weights, 2)

#add the total weights from each assesment to the total weights
total_weights = pre_class_total_weights + class_total_weights + assignment_total_weights + test_total_weights
#add each total mark for each assesment to the variable
total_mark = pre_class_sum  + class_exercise_sum + assignment_sum + test_sum
# dvidide the total marks by the total weights
total_mark = total_mark / total_weights

#Display the rounded output for the total mark
print("the mid-term calculated weighted average is:", round(total_mark), "%")