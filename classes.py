import json

# Allowed parts of speech
allowed_parts_of_speech = ["noun", "verb", "adjective", "adverb", "pronoun", "preposition", "conjunction", "interjection"]

# Initialize or load the dictionary
try:
    with open('custom_dictionary.json', 'r') as file:
        dictionary = json.load(file)
except FileNotFoundError:
    dictionary = {}

# Function to add or update a word
def add_or_update_word(word, definition=None, part_of_speech=None, synonyms={}):
    if part_of_speech and part_of_speech.lower() not in allowed_parts_of_speech:
        print(f"Invalid part of speech. Allowed options are: {', '.join(allowed_parts_of_speech)}")
        return
    dictionary[word] = {
        "definition": definition,
        "part_of_speech": part_of_speech,
        "synonyms": synonyms
    }

# Function to save changes
def save_dictionary():
    with open('custom_dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=4)

# Example usage
add_or_update_word("example", "a thing characteristic of its kind", "noun", {"sample": "high"})
save_dictionary()

       
