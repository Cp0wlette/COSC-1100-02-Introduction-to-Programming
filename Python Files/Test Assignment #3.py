# create a list of words to use as replacements
emoji = ("0", "💯", "😠", "🍎", "🍌", "🐦", "🧠", "🚌", "🚗", "🥕","🐈", "👏", "🥶", "🍪", "🐕", "🥚", "🐟", "🦊", "😀", "❤", "🐎", "🥵", "🗺", "👌", "😢", "🛌", "🌲", "🧟")

# create a dictionary that maps each word in the message to a word in the list
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
    "hot" : emoji[19],
    "cold" : emoji[20],
    "map" : emoji[21],
    "OK" : emoji[22],
    "sad" : emoji[23],
    "sleep" : emoji[24],
    "tree" : emoji[25],
    "zombie" : emoji[26],   
}
# define a function that encrypts a message using the cipher dictionary
def encrypt():
    global user_input
    i = 0
    # split the message into words
    words = user_input.split()
    # create an empty list to store the encrypted words
    encrypted = []
    # loop through each word in the message
    for i in range(len(user_input)):
        # check if the word is in the cipher dictionary
        if user_input[i+1] in emoji_dictionary:
            # replace the word with the corresponding word in the list
            encrypted.append(emoji_dictionary[i])
            print(encrypted)
        else:
            # if the word is not in the dictionary, keep it as it is
            i += 1
            continue
    # join the encrypted words into a single string
    encrypted_message = " ".join(encrypted)
    # return the encrypted message
    return encrypted_message

# get the user input
user_input = input("Enter a message to encrypt: ")

# encrypt the user input
encrypted_message = ""

# print the encrypted input
print("The encrypted message is:", encrypted_message)
