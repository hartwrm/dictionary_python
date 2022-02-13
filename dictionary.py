import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s :" %get_close_matches(word, data.keys())[0])
        decide = input("press y/n\n")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Sorry, this word is not in the dictionary")
        else: 
            return("you have entered the wrong input, try again")

word = input("Enter your search word: \n")
output = search(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
