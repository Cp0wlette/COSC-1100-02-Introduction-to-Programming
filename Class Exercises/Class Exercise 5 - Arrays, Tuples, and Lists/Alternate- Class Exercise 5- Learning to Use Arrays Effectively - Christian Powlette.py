# Filename: Alternate- Class Exercise 5- Learning to Use Arrays Effectively - Christian Powlette
# Date: 2023-11-3
# Christian Powlette
# Description: A program to prompt a user to enter a their marks for a varierty of assesments to calculte their current mid-term mark.

# DECLARATIONS

#Constants
PRE_AND_IN_CLASS_ACTIVITY_WEIGHT = 3
ASSIGNMENTS_WEIGHT = 10
TEST_WEIGHT = 12


#Variables
#Variable for final output weighted average mark
total_mark = 0
#Variables for the user's input for each assesment
pre_class_activity_input = 0
class_exercise_input = 0
assignments_input = 0
test_input = 0
#Variables for the calculated weighted mark
pre_class_weighted_mark = 0
class_weighted_mark = 0
assignment_weighted_mark = 0
test_weighted_mark = 0
#Variables for total weights
pre_class_total_weights = 0
class_total_weights = 0
assignment_total_weights = 0
test_total_weights = 0

#Variables for each assesment list containing each mark obtained by the user's input variable
markslist= [0]
pre_class_activities = [0]
class_exercises = [0]
assignments = [0]
test = [0]

#Variable determing the running  status of the while loop
session = 1
while session != 0:
    #Print space line
    print("")
    print("Please enter your mark for the various assesments ")
    print("")
    for i in range(5):
        print("These past weeks we have had;")
        print("5 pre-class activies")
        markslist_input = input("Please enter mark(s) accordingly ")
        try:
            markslist_input = int(markslist_input)
        except ValueError:
            print("ERROR enter a numeric value")
            continue
        print(markslist)
        markslist.append(markslist_input * PRE_AND_IN_CLASS_ACTIVITY_WEIGHT)
    for i in range(4):
        print("These past weeks we have had;")
        print("4 class exercises (not including this one)")
        markslist_input = input("Please enter mark(s) accordingly ")
        try:
            markslist_input = int(markslist_input)
        except ValueError:
            print("ERROR enter a numeric value")
            continue
        markslist.append(markslist_input [5 + i] * PRE_AND_IN_CLASS_ACTIVITY_WEIGHT)

    print("These past weeks we have had;")
    print("1 assignment")
    markslist_input = input("Please enter mark accordingly ")
    try:
        markslist_input = int(markslist_input)
    except ValueError:
        print("ERROR enter a numeric value")
        continue
    markslist.append(markslist_input[9+i] * ASSIGNMENTS_WEIGHT)

    print("These past weeks we have had;")
    print("1 test")
    markslist_input = input("Please enter mark accordingly ")
    try:
        markslist_input = int(markslist_input)
    except ValueError:
        print("ERROR enter a numeric value")
        continue
    markslist.append(test_input[10+ i] * TEST_WEIGHT)
    break

total_mark = sum(markslist)
pre_class_total_weights = PRE_AND_IN_CLASS_ACTIVITY_WEIGHT * 5
class_total_weights = PRE_AND_IN_CLASS_ACTIVITY_WEIGHT * 4
assignment_total_weights = ASSIGNMENTS_WEIGHT 
test_total_weights = TEST_WEIGHT
total_weight =   pre_class_total_weights + class_total_weights + assignment_total_weights + test_total_weights

total_mark *= total_weight


#OUTPUT
print("the mid-term weighted average is:", round(total_mark), "%")