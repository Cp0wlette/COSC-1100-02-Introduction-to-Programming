emoji_english = {"100","angry", "apple", "banana", "bird", "brain", "bus", "car", "carrot", "cat", "clap", "cold",
                  "cookie", "dog", "egg", "fish", "fox", "happy", "heart", "horse" "hot", "map", "OK", "sad", "sleep", 
                  "tree", "zombie"}
emoji = ("💯", "😠", "🍎", "🍌", "🐦", "🧠", "🚌", "🚗", "🥕","🐈", "👏", "🥶", "🍪", "🐕", "🥚", "🐟", "🦊",
          "😀", "❤", "🐎", "🥵", "🗺", "👌", "😢", "🛌", "🌲", "🧟")
 

emoji_dictionary = {
    "100": emoji[0],
    "angry" : emoji[1],
    "apple" : emoji[2],
    "banana" : emoji[3],
    "bird" : emoji[4],
    "brain" : emoji[5],
    "bus" : emoji[6],
    "car" : emoji[7],
    "carrot" : emoji[8],
    "cat" : emoji[9],
    "clap" : emoji[10],
    "cold" : emoji[11],
    "cookie" : emoji[12],
    "dog" : emoji[13],
    "egg" : emoji[14],
    "fish" : emoji[15],
    "fox" : emoji[16],
    "happy" : emoji[17],
    "heart" : emoji[18],
    "horse" : emoji[19],
    "hot" : emoji[20],
    "map" : emoji[21],
    "OK" : emoji[22],
    "sad" : emoji[23],
    "sleep" : emoji[24],
    "tree" : emoji[25],
    "zombie" : emoji[26],   
}

# define a function that switches certain words with numbers in a tuple
def switch_words(input_string):
    # split the input string into words
    words = input_string.split()
    # create an empty list to store the modified words
    modified = []
    # loop through each word in the input string
    for word in words:
        # check if the word is in the word dictionary
        if word in emoji_dictionary:
            # replace the word with the corresponding number in the tuple
            modified.append(str(emoji_dictionary[word]))
        else:
            # if the word is not in the dictionary, keep it as it is
            modified.append(word)
    # join the modified words into a single string
    modified_string = " ".join(modified)
    # return the modified string
    return modified_string

# get the user input
user_input = input("Enter a string: ")

# switch the words with the numbers in the tuple
switched_input = switch_words(user_input)

# print the switched input
print("The switched string is:", switched_input)


