# Filename: Assignment 2 - Secret Codes (Arrays & Functions) - Christian Powlette
# Date: 2023-11-14
# Christian Powlette
# Description: A program to prompt a user to encode, decode, or exit the program / while loop

#DECLARATIONS

# defines function to encode the input the user provides

def encode_user_input():
    # makes emoji_dictionary global
    global emoji_dictionary
    #store user input in variable, and diplay prompt
    user_input_encode = input("Enter a string to encode: ")
    # split the input string into words
    english = user_input_encode.split()
    # create an empty list to store the modified words
    encoded = []
    # loop through each word in the input string
    for word in english:
        # check if the word is in the emoji dictionary
        if word in emoji_dictionary:
            # replace the word with the corresponding element in the tuple
            encoded.append(emoji_dictionary[word])
        else:
            encoded.append(word)
    # join the modified words into a single string
    encoded_modified_string = " ".join(encoded)
    # return the modified string
    return encoded_modified_string

# defines a function that decodes user_input 
def decode_user_input():
    # prints a prompt and stores the user's input
    user_input_decode = input("Enter a string to decode: ")
    # split the input string into words
    encoded_list = user_input_decode.split()
    # create an empty list to store the decoded words
    decoded = []
    # loop through each word in the input string for the length of the encoded_list
    for char in range(len(encoded_list)):
        # store specfic emoji or "char" index of the encoded_list  in letter
        letter = encoded_list[char]
        # sets match found equal to false
        match_found = False
        # loop for each emoji index in the range of the length of the emoji
        for emoji_index in range(len(emoji)):
            # if the variable "letter" is equal to the element in the emoji index then do the following:
            if letter == emoji[emoji_index]:
                # replace the word with the corresponding index in the tuple
                decoded.append(emoji_english[emoji_index])
                # set match found equal to True
                match_found = True
        # if match  found is equal to False, then do the following:
        if match_found == False:
            #append the element to the decoded string
            decoded.append(letter)
    # join the decoded and modified words string with the decoded list
    decoded_modified_string = " ".join(decoded)
    # return the decoded and  modified string
    return decoded_modified_string

# VARIABLES

# variable that decides which option the user chooses
user_input = 0
#prints the prompt to diplay the options the user can access
prompt = '''
1) Enter 1 to Encode
2) Enter 2 to Decode
3) Enter 3 to Exit'''

# Array that contains the english translation of various emojis (0-26)
emoji_english = ("100","angry", "apple", "banana", "bird", "brain", "bus", "car", "carrot", "cat", "clap", "cold","cookie", "dog", "egg", "fish", "fox", "happy", "heart", "horse", "hot", "map", "OK", "sad", "sleep", "tree", "zombie")

# Array that contains the emoji translation of various emojis (0-26)
emoji = ("💯", "😠", "🍎", "🍌", "🐦", "🧠", "🚌", "🚗", "🥕","🐈", "👏", "🥶", "🍪", "🐕", "🥚", "🐟", "🦊", "😀", "❤", "🐎", "🥵", "🗺", "👌", "😢", "🛌", "🌲", "🧟")

# English dictionary that contains a translation  between emojis to enlgish (0-26) 
english_dictionary = {"💯" : emoji_english[0], "😠" : emoji_english[1],"🍎" : emoji_english[2],"🍌" : emoji_english[3],"🐦" : emoji_english[4],"🧠" : emoji_english[5],"🚌" : emoji_english[6],"🚗" : emoji_english[7],"🥕" : emoji_english[8],"🐈" : emoji_english[9],"👏" : emoji_english[10],"🥶" : emoji_english[11],"🍪" : emoji_english[12],"🐕" : emoji_english[13],"🥚" : emoji_english[14],"🐟" : emoji_english[15],"🦊" : emoji_english[16],"😀" : emoji_english[17],"❤"  : emoji_english[18],"🐎" : emoji_english[19],"🥵" : emoji_english[20],"🗺" : emoji_english[21],"👌" : emoji_english[22],"😢" : emoji_english[23],"🛌" : emoji_english[24],"🌲" : emoji_english[25],"🧟" : emoji_english[26]}

# English dictionary that contains a translation between emojis to enlgish (0-30), includes 4 duplicate emoji transaltions
emoji_dictionary = {"100": emoji[0], "angry" : emoji[1], "apple" : emoji[2], "banana" : emoji[3], "bird" : emoji[4], "brain" : emoji[5],"bus" : emoji[6], "car" : emoji[7], "carrot" : emoji[8], "cat" : emoji[9], "clap" : emoji[10], "cold" : emoji[11], "cookie" : emoji[12], "dog" : emoji[13], "egg" : emoji[14], "fish" : emoji[15], "fox" : emoji[16], "happy" : emoji[17], "heart" : emoji[18], "horse" : emoji[19], "hot" : emoji[20], "map" : emoji[21], "OK" : emoji[22], "sad" : emoji[23], "sleep" : emoji[24], "tree" : emoji[25], "zombie" : emoji[26],  "100%" : emoji[0], "mad" : emoji[1], "okay" : emoji[22], "bed" : emoji[24],}

# A while loop to display options for the user to access and prints the functions of the options the user chooses
while user_input != "3":
    #prints primary prompt for user
    print("")
    print("Enter one of the following numerical values")
    # prints secodnary prompt for user that diplays options
    print(prompt)
    print("")
    # stores user input that decides which options the user chooses
    user_input = input("Option: ")
    # option that equals encoding the english string the user will choose
    if user_input == "1":
        print("")
        # prints the output from the function that encodes the user's input
        print("The encoded message is: ", encode_user_input())
    # option that equals decoding the emoji string the user will choose
    elif user_input == "2":
        print("")
        # prints the output from the function that decodes the user's input
        print("The decoded message is: ", decode_user_input())
    # option that equals ending the program
    elif user_input == "3":
        print("")
        # prints a conclusion final message to program
        print("Exiting Decoder and Encoder program")
    elif user_input != "1" or "2" or "3":
        # diplays error if the user enters a input outside the range of options they can choose
        print("")
        print("Invalid input")


        