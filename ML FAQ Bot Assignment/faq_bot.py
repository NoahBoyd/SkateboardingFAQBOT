""" This is a very simple skeleton for a FAQ bot, based on the handout given in
class. Your job is to create your own FAQ bot that can answer 20 questions
using basic string matching. See the handout for more details.

When you create your bot you can adapt this code or start from scratch and
write your own code.

If you adapt this code, add yourself below as author and rewrite this header
comment. See the Resources folder on Canvas for documentation standards.

Noah Boyd, 09-23-2022
"""

import string
import regex as re
import spacy
from spacy.matcher import Matcher 
# nlp = spacy.load("en_core_web_sm") 
nlp = spacy.load("en_core_web_lg")
print("Spacy Loaded")
def load_FAQ_data():
    """This method returns a list of questions and answers. The
    lists are parallel, meaning that intent n pairs with response n."""

    # return file_input('questions_regex.txt'), file_input('answers.txt', False)
    return file_input('ML_Questions.txt'), file_input('ML_Answers.txt', False) # New line in ML BOT
    

def file_input(filename, doStrip=True):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            if (doStrip):
                # lineStripped = stripPunctuation(line).lower()    OLD FROM BEFORE REGEX
                lineStripped = line.lower()
                lines.append(lineStripped.strip())
            else:
                lines.append(line.strip()) # the strip method removes extra whitespace
    return lines

# RETURN ARRAY [INDEX, UTTERANCE] to be used with SpaCy
"""
This function takes a string as input and returns that string with punctuation stripped out of it
"""
def stripPunctuation(stringInput):
    # stringStripped = ''.join([letter for letter in string if letter in ascii_letters])
    return stringInput.translate(str.maketrans('', '', string.punctuation))
    # print("This is strip punctuation: " + stringStripped)

def understand(utterance):
    """This method processes an utterance to determine which intent it
    matches. The index of the intent is returned, or -1 if no intent
    is found."""

    global intents # declare that we will use a global variable
    utterance = stripPunctuation(utterance).lower().strip() # Normalize utterance
    # check if hello or goodbye
    if utterance == "goodbye" or utterance == "quit":
        return ['quit', utterance]
    if utterance == "hello":
        return ['hello', utterance]


    tempUtterance = utterance
    # Vectorize Utterance
    newVector = vectorizor.transform([tempUtterance]);
    # print(newVector.toarray())
    from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
    cosine_sim = cosine_similarity(newVector, vectors)
    # print(cosine_sim)
    maxSim = 0
    maxSimIndex = 0
    for i in range(len(cosine_sim)):
        for j in range(len(cosine_sim[i])):
            if cosine_sim[i][j] > maxSim:
                maxSim = cosine_sim[i][j]
                maxSimIndex = j
        
    # print(maxSim)
    # print(maxSimIndex)
    if (maxSim > 0.5):
        return [maxSimIndex, utterance]
    else: 
        return [-1, utterance]
    # try to index utterance
    # try:
    #     # Check utterance against array of regex patterns
    #     matches_found = 0
    #     best_match = ""
    #     matches = []
    #     for idx, intent in enumerate(intents):
    #         pattern = r"({}){}".format(intent, "{e<=2}")
    #         m=re.search(pattern, utterance) 
    #         if (m != None): # check if match
    #             matches_found += 1
    #             matches.append([idx, m.fuzzy_counts])
    #     if (matches_found == 0): # No matches found
    #         return [-1, utterance]
    #     elif (matches_found == 1): # One match was found
    #         return [int(matches[0][0]), utterance]
    #     elif (matches_found > 1): # More than one match found
    #         # Find the best match
    #         best_match = findBestMatch(matches)
    #         return [int(best_match), utterance]

    # except ValueError:
    #     return -1

def findBestMatch(matches):
    bestRating = 0
    bestMatch = None
    for match in matches:
        rating = sum(match[1])
        if (bestRating == 0):
            bestRating = rating
            bestMatch = match[0]
        if (rating < bestRating):
            bestMatch = match[0]
            bestRating = rating
    return bestMatch

        

def generate(intent):
    """This function returns an appropriate response given a user's
    intent."""

    global responses # declare that we will use a global variable
    
    if intent[0] == -1: # No match found, use Spacy to try to come up with a response
        response1 = generateSpacyResponse(intent[1])
        msg = ""
        response = determineSentiment(intent[1])
        if (response[0] == 0):
            # return "I'm sorry you feel that way..."
            msg += "I'm sorry you feel that way...\n"
        elif (response[0] == 1):
            msg += "Thats Great!\n"
        msg += response1
        return msg
    elif intent[0] == 'quit': # Quit the program
        return "Self destruct protocol activated... Goodbye!"
    elif intent[0] == 'hello': # Greet the user
        return "Hello! Please ask me some questions about skateboarding."

    return responses[intent[0]]

def determineSentiment(utterances):
    utterances = [utterances]
    newTest = [doc.vector for doc in nlp.pipe(utterances)]
    newP = pClf.predict(newTest)
    return newP

def generateSpacyResponse(utterance):
    doc = nlp(utterance)
    response = ""
    # Pattern to match user asking about a location
    pattern = [
        {"LEMMA": "go"},   
        {"LOWER": {"IN": ["to", "into", "toward"]}},   
        {"POS": "DET"},   
        {"POS": {"IN": ["ADJ", "PUNCT"]}, "OP": "*"}, 
        {"POS": "NOUN"}    
    ]   

    # pattern to match user asking for directions to somewhere
    pattern2 = [
        {"LEMMA": "direction"},
        {"LOWER": "to"},
        {"POS": "DET"},
        {"POS": {"IN": ["ADJ", "PUNCT"]}, "OP": "*"}, 
        {"POS": "NOUN"}
    ] 
    # Add patterns to matcher
    matcher = Matcher(nlp.vocab) 
    matcher.add("location phrase", [pattern]) 
    matcher.add("direction phrase", [pattern2]) 

    # Check for matches
    matches = matcher(doc)
    if (len(matches) > 0):
        # Get the type of pattern it matched
        matchType = nlp.vocab.strings[matches[0][0]]
        if (matchType == "direction phrase"):
            start = matches[0][1]
            end = matches[0][2]
            matchText = doc[start+2:end]
            response = "If you want directions to {}, you should consider buying a GPS".format(matchText)
            return response
        elif (matchType == "location phrase"):
            start = matches[0][1]
            end = matches[0][2]
            matchText = doc[start+2:end]
            response = "Sorry I dont know, I've never been to the {}".format(matchText)
            return response
    else: 
        # Do some other type of check now

        # Check for named entities 
        
        if (len(doc.ents) >= 1):
            if (doc.ents[0].label_ == "GPE"):
                response = "Sorry I'm not sure. I've never been to {}".format(doc.ents[0])
                return response
            elif (doc.ents[0].label_ == "PERSON"):
                response = "Sorry I'm not sure. I've never met {}".format(doc.ents[0])
                return response

        # Check for noun chunks if there is no entities
        elif (len(doc.ents) == 0):
            longestNounChunk = 0
            longestNounChunkText = ""
            for np in doc.noun_chunks:
                if (len(np.text) > longestNounChunk):
                    longestNounChunk = len(np.text)
                    longestNounChunkText = np.text
            if (longestNounChunk > 0):
                response = "I dont have any information about {}, can you be more specific?".format(longestNounChunkText)
                return response
            else:
                response = "Sorry, I don't know how to answer that."
                return response
    return response

    
## Load the questions and responses
intents, responses = load_FAQ_data()

## Run 'intents' through CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
vectorizor = CountVectorizer(max_df=0.5)
vectors = vectorizor.fit_transform(intents)
print("Vectors Loaded")

## Load the Pickeled Model
from joblib import load
pClf = load('sentiment_classifier.pkl')
# doc1 = ["This is a great bot"]
# newTest = [doc.vector for doc in nlp.pipe(doc1)]
# newP = pClf.predict(newTest)
# print("Prediction is: ")
# print(newP)

## Main Program


"""
This method is used to demonstrate the functionality of the script
It uses input from the user to generate an utterance, then generates the intent of the utterance, finally it creates a response based on
the intent and prints it out for the user
"""
def chat():
    # talk to the user
    print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")
    print()
    utterance = ""
    while True:
        utterance = input(">>> ")
        utterance = stripPunctuation(utterance).lower().strip() # Normalize utterance
        if utterance == "goodbye" or utterance == "quit":
            break;
        if utterance == "hello":
            print("Hello!\n")
            continue;
        intent = understand(utterance)
        response = generate(intent)
        print(response)
        print()

    print("Nice talking to you!")

# Uncomment the line below to run in terminal
# chat()


