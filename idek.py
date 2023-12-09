import argparse
from typing import List
import requests

from main import CustomDictionary

class WordEntry:
    def __init__(self, word: str = '', definition: str = '', synonyms: List[str] = [], part: str = '') -> None:
        """
        Initialize the class with the given word, definition, synonyms, and part of speech.
        Args:
        word (str): The word.
        definition (str): The definition of the word.
        synonyms (List[str]): A list of synonyms for the word.
        part (str): The part of speech of the word.
        """
        self.word = word
        self.definitions = [{'part': part, 'definition': definition}] if part and definition else []
        self.synonyms = synonyms
        self.part = part

    def add_def(self, part: str, definition: str):
        # Optionally check for duplicates before appending
        self.definitions.append({'part': part, 'definition': definition})


    def add_part(self, part):
        self.part = part
        
    def add_synonyms(self, synonyms: List[str]):
        # Optionally check for duplicates before extending
        self.synonyms.extend(synonyms)

    def __str__(self):
        definitions_str = '\n'.join(f"{d['part']}: {d['definition']}" for d in self.definitions)
        synonyms_str = ', '.join(self.synonyms)
        return f"{self.word}\nDefinitions:\n{definitions_str}\nSynonyms: {synonyms_str}"

class CustomDictionary:
    def __init__(self):
        self.word_entries = {}

    def add_word(self, word: str, definition: str, synonyms: List[str], part: str):
        if word in self.word_entries:
            self.word_entries[word].add_def(part, definition)
            self.word_entries[word].add_synonyms(synonyms)
        else:
            self.word_entries[word] = WordEntry(word, definition, synonyms, part)

    def find_word_entry(self, word: str):
        if word in self.word_entries:
            return self.word_entries[word]
        else:
            return None
    
    def load_dictionary(self):
        pass
    
    def save_dictionary(self):
        pass
    
    

def fetch_definition(word):
    # Implement API call here
    # Return the definition
    pass

def main():
    my_dict = CustomDictionary()
    my_dict.load_dictionary()
     
    while True:
        command = input("Enter command (add, define, synonyms, save, quit): ").lower()
        if command == "add":
            choice = input("Enter '1' to input definition manually, '2' to retrieve from API: ")
            
            if choice == '1':
                word = input("Enter word: ")
                part = input("Enter part of speech: ")
                definition = input("Enter definition: ")
                my_dict.add_word(word, definition, [], part)
                print(f"Your definition for {word}: {definition}")
            elif choice == '2':
                word = input("Enter word: ")
                definition = fetch_definition(word)
                print(f"The definition of {word}: {definition}")
            else:
                print("Invalid choice.")
            my_dict.add_word(word, part, definition)
            print("Word added.")
            
                
        elif command == "define":
            word = input("Enter word to define: ")
            entry = my_dict.find_word_entry(word)
            if entry:
                print(entry)
            else:
                print(f"No definition found for '{word}'.")
                if input("Would you like to add it? (y/n): ").lower() == 'y':
                    part = input("Enter part of speech: ")
                    definition = input("Enter definition: ")
                    my_dict.add_word(word, definition, [], part)
                    print("Word added.")
                else:
                    print("Definition not added.") 
                    
        elif command == "delete":
            word = input("Enter word to delete: ")
            if input(f"Are you sure you want to delete '{word}'? (y/n): ").lower() == 'y':
                my_dict.delete_word(word)
                print("Word deleted.")
            else:
                print("Word not deleted.")
            
        elif command == "update":
            word = input("Enter word to update: ")
            part = input("Enter part of speech: ")
            definition = input("Enter new definition: ")
            my_dict.update_word(word, part, definition)
            print(f"Definition for '{word}' updated.")
            
            
        elif command == "synonyms":
            word = input("Enter word to find synonyms: ")
            synonyms = input("Enter synonyms separated by commas: ").split(',')
            my_dict.add_synonyms(word, synonyms)
            print(f"Synonyms for '{word}' updated.")
            
        elif command == "save":
            my_dict.save_dictionary()
            print("Dictionary saved.")
            
        elif command == "quit":
            break
        
    


# def main():
#     my_dict = CustomDictionary()
#     my_dict.load_dictionary()

#     while True:
#         command = input("Enter command (add, define, synonyms, save, quit): ").lower()
#         if command == "add":
#             word = input("Enter word: ")
#             part = input("Enter part of speech: ")
#             definition = input("Enter definition: ")
#             my_dict.add_word(word, definition, [], part)
#         elif command == "define":
#             word = input("Enter word to define: ")
#             definitions = my_dict.get_definitions(word)
#             if isinstance(definitions, str):
#                 print(definitions)
#             else:
#                 for part, definition in definitions:
#                     print(f"{part}: {definition}")
#         elif command == "synonyms":
#             word = input("Enter word to find synonyms: ")
#             synonyms = input("Enter synonyms separated by commas: ").split(',')
#             my_dict.add_synonyms(word, synonyms)
#         elif command == "save":
#             my_dict.save_dictionary()
#             print("Dictionary saved.")
#         elif command == "quit":
#             break
        
        
if __name__ == "__main__":
    main()
