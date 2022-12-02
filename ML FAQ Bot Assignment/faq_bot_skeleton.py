""" This is a very simple skeleton for a FAQ bot, based on the handout given in
class. Your job is to create your own FAQ bot that can answer 20 questions
using basic string matching. See the handout for more details.

When you create your bot you can adapt this code or start from scratch and
write your own code.

If you adapt this code, add yourself below as author and rewrite this header
comment. See the Resources folder on Canvas for documentation standards.

YOUR NAME AND DATE
Sam Scott, Mohawk College, May 2021
(Modified January 11, 2022: Removed some unnecessary global declarations)
"""

import string

def load_FAQ_data():

    return file_input('questions.txt'), file_input('answers.txt')


def file_input(filename):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            # lines.append(line.strip()) # the strip method removes extra whitespace  
            lineStripped = stripPunctuation(line).lower()
            # print(lineStripped)
            lines.append(lineStripped)
    return lines


def stripQuestionMark(utterance):
    if utterance[-1] == "?":
        return utterance.rstrip(utterance[-1])
    return utterance

def stripPunctuation(stringInput):
    # stringStripped = ''.join([letter for letter in string if letter in ascii_letters])
    return stringInput.translate(str.maketrans('', '', string.punctuation))
    # print("This is strip punctuation: " + stringStripped)

def understand(utterance):
    """This method processes an utterance to determine which intent it
    matches. The index of the intent is returned, or -1 if no intent
    is found."""


    global intents # declare that we will use a global variable

    try:
        # return intents.index(utterance)
        # return [string.lower() for string in intents].index(stripQuestionMark(utterance)) # this is changed to index based the array items in lowercase
        utteranceStripped = stripPunctuation(utterance).strip()
        # print("Stripped = " + utteranceStripped)
        print(utteranceStripped)

        for intent in intents:
            if (intent == utteranceStripped):
                print("MATCH: " + intent[utteranceStripped])

        return intents.index(utteranceStripped)
    except ValueError:
        return -1

def generate(intent):
    """This function returns an appropriate response given a user's
    intent."""

    global responses # declare that we will use a global variable

    if intent == -1:
        return "Sorry, I don't know the answer to that!"

    return responses[intent]

## Load the questions and responses
intents, responses = load_FAQ_data()
# for intent in intents:
#     print(intent)

for response in responses:
    print(response)

## Main Program

def chat():
    # talk to the user
    print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")
    print()
    utterance = ""
    while True:
        utterance = input(">>> ").lower() # Changed to get lowercase of input
        if utterance == "goodbye":
            break;
        intent = understand(utterance)
        response = generate(intent)
        print(response)
        print()

    print("Nice talking to you!")

 # added this line to start the program in the shell
chat();