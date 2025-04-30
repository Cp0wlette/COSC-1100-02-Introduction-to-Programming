# Filename: Class Exercise 5- Learning to Use Arrays Effectively - Christian Powlette
# Date: 2023-11-3
# Christian Powlette
# Description: A program to prompt a user to enter a their marks for a varierty of assesments to calculte their current mid-term mark.

# DECLARATIONS
def get_average_input(assignment_type: list = [], weight_type: int = 0, iteration_type: int = 0, assignment_text: str = "Default"):
    for i in range(iteration_type):
        print("Please enter your numeric integer mark for the", assignment_text, "assesment")
        average_input = input()
        try:
            average_input = int(average_input)
            # if it cannot turn into a integer print the following ERROR message
        except ValueError:
            print("ERROR enter a numeric value")
        assignment_type.append(average_input * weight_type)
        print(assignment_type)
    return assignment_type
    
def calculate_weighted_average(assignment_type: list = [], weight_type: int = 0, total_weights_type: int = 0, assignment_mark_type: int = 0, iteration_type: int = 0):
    assignment_mark_type
    total_weights_type = 0
    for i in range(iteration_type):
        # calculate the sum from each mark element in the list
        assignment_mark_type = sum(assignment_type)
        # add the weights to the total weight to get total
        total_weights_type += weight_type
    return total_weights

#def displayoutput():
    
#Constants
Pre_class_text = "Please enter your numeric integer mark for the Pre class assignment"
# Pre class activity and the class exercises weight = 3%
# Aassignment weight = 1-%
# Test weight = 6%
weight_type = 0
iteration_type = 0
total_weights = 0
assignment_type = 0
#Variables
#Variable for final output weighted average mark
total_mark = 0
pre_class_mark = 0
class_exercise_mark = 0
assignment_mark = 0
test_mark = 0

#Variables for total weights
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
    #if the list has one element (0) than do the following
    get_average_input(pre_class_activities, 3, 5, "pre class activity")
    get_average_input(class_exercises, 3, 4, "class exercise")
    get_average_input(assignments, 10, 1, "assignment")
    get_average_input(test, 6, 2, "test")
    # once done / checking the following break and get out of loop
    break
calculate_weighted_average(pre_class_activities, 3, pre_class_total_weights, pre_class_mark, 5)
calculate_weighted_average(class_exercises, 3, class_total_weights, class_exercise_mark, 4)
calculate_weighted_average(assignments, 10, assignment_total_weights, assignment_mark, 1)
calculate_weighted_average(test, 12, test_total_weights, test_mark, 2)
# repeat the following  4 times


#add the total weights from each assesment to the total weights
print(pre_class_total_weights, class_total_weights, assignment_total_weights, test_total_weights)
total_weights = pre_class_total_weights + class_total_weights + assignment_total_weights + test_total_weights
print(total_weights)
#add each total mark for each assesment to the variable
total_mark = (pre_class_mark  + class_exercise_mark + assignment_mark + test_mark) 
print(total_weights)
# dvidide the total marks by the total weights
total_mark = total_mark / total_weights

#Display the rounded output for the total mark
print("the mid-term weighted average is:", round(total_mark), "%")