# Filename: Class Exercise 5- Learning to Use Arrays Effectively - Christian Powlette
# Date: 2023-11-3
# Christian Powlette
# Description: A program to prompt a user to enter a their marks for a varierty of assesments to calculte their current mid-term mark.

# DECLARATIONS

#Constants
# constant for the weight of the pre class acitivy and the class exercise
PRE_AND_IN_CLASS_ACTIVITY_WEIGHT = 3
# constant for the weight of the assignment
ASSIGNMENTS_WEIGHT = 10
# constant for the weight of the test
TEST_WEIGHT = 12

#Variables
#Variable for final output weighted average mark
total_mark = 0

#Variables for the user's input for each assesment
pre_class_activity_input = 0
#class exercise input varibale
class_exercise_input = 0
# assignment input variable
assignments_input = 0
# test input variable
test_input = 0

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
    if len(pre_class_activities) == 1:
        # repeat the following steps 5 times
        for i in range(5):
            # prompt the user to enter input
            pre_class_activity_input = input("Please enter your numeric integer mark for the pre-class activity assesments ")
            #try to turn input into integer
            try:
                pre_class_activity_input = int(pre_class_activity_input)
            except ValueError:
                # if it cannot turn into a integer print the following ERROR message
                print("ERROR enter a numeric value")
                continue
            pre_class_activities.append(pre_class_activity_input * PRE_AND_IN_CLASS_ACTIVITY_WEIGHT)
    #if the list has one element (0) than do the following
    elif len(class_exercises) == 1:
        # repeat the following steps 4 times
        for i in range(4):
            # prompt the user to enter input
            class_exercise_input = input("Please enter your numeric integer mark for the class exercise assesments ")
            #try to turn input into integer
            try:
                class_exercise_input = int(class_exercise_input)
            # if it cannot turn into a integer print the following ERROR message
            except ValueError:
                print("ERROR enter a numeric value")
                continue
            class_exercises.append(class_exercise_input * PRE_AND_IN_CLASS_ACTIVITY_WEIGHT)
    #if the list has one element (0) than do the following
    elif len(assignments) == 1:
        # repeat the following steps once
        for i in range(1):
            # prompt the user to enter input
            assignments_input = input("Please enter your numeric integer mark for the assignment ")
            #try to turn input into integer
            try:
                assignments_input = int(assignments_input)
            except ValueError:
                # if it cannot turn into a integer print the following ERROR message
                print("ERROR enter a numeric value")
                continue
            assignments.append(assignments_input * ASSIGNMENTS_WEIGHT)
    #if the list has one element (0) than do the following
    elif len(test) == 1:
        # repeat the following steps once
        for i in range(2):
            # prompt the user to enter input
            test_input = input("Please enter your numeric integer mark for the test ")
            #try to turn input into integer
            try:
                test_input = int(test_input)
            except ValueError:
                # if it cannot turn into a integer print the following ERROR message
                print("ERROR enter a numeric value ")
                continue
            test.append(test_input * TEST_WEIGHT)
    # once done / checking the following break and get out of loop
    else:
        break
# repeat the following  5 times
for i in range(5):
    # calculate the sum from each mark element in the list
    pre_class_mark = sum(pre_class_activities)
    # add the weights to the total weight to get total
    pre_class_total_weights += PRE_AND_IN_CLASS_ACTIVITY_WEIGHT

# repeat the following  4 times
for i in range(4):
    # calculate the sum from each mark element in the list
    class_exercise_mark = sum(class_exercises)
    # add the weights to the total weight to get total
    class_total_weights += PRE_AND_IN_CLASS_ACTIVITY_WEIGHT

# repeat the following  once
for i in range(1):
    # calculate the sum from each mark element in the list
    assignment_mark = sum(assignments)
    # add the weights to the total weight to get total
    assignment_total_weights += ASSIGNMENTS_WEIGHT

# repeat the following  2 times
for i in range(2):
   # calculate the sum from each mark element in the list
    test_mark = sum(test)
    # add the weights to the total weight to get total
    test_total_weights += TEST_WEIGHT

#add the total weights from each assesment to the total weights
total_weights = pre_class_total_weights + class_total_weights + assignment_total_weights + test_total_weights
#add each total mark for each assesment to the variable
total_mark = (pre_class_mark  + class_exercise_mark + assignment_mark + test_mark) 
# dvidide the total marks by the total weights
total_mark = total_mark / total_weights

#Display the rounded output for the total mark
print("the mid-term weighted average is:", round(total_mark), "%")

