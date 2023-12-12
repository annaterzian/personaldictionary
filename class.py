from typing import List
import json


class DictionaryEntry:
    def __init__(self, word: str = '', definition: str = '', synonyms: List[str] = [], partOfSpeech: str = ''):
        self.word = word
        self.definition = [{'definition': definition, 'partOfSpeech': partOfSpeech}] if partOfSpeech and definition else []
        self.synonyms = synonyms

    def __str__(self):
    #Returns a user friendly representation of the object
        definition = self.definitions[0]  # Select the first definition
        definitions_str = f"{definition['part']}: {definition['definition']}"
        synonyms_str = ', '.join(self.synonyms)
        return f"{self.word}\nDefinition:\n{definitions_str}\nSynonyms: {synonyms_str}"

    def __repr__(self):
    # Returns a developer friendly representation of the object
        return self.word

    def add_word(self, word: str) -> None:
    # Add a word
        self.word = word
        print("Word added successfully.")
        return

    def add_definition(self, definition: str, partOfSpeech: str) -> None:
    # Check if the definition already exists (irrespective of partOfSpeech)
        for existing_definition in self.definitions:
            if existing_definition['definition'] == definition:
                print("This definition already exists.")
                return
        # Add the new definition    
        self.definition.append({'definition': definition, 'partOfSpeech': partOfSpeech})
        print("Definition added successfully.")
        return

    def add_synonym(self, synonym: str) -> None:
    # Add a synonym
        self.synonyms.append(synonym)
        print("Synonym added successfully.")
        return

    def add_part(self, partOfSpeech: str, definition: str = '') -> None: 
    # Add a part of speech
        self.definition.append({'definition': definition, 'partOfSpeech': partOfSpeech})
        print("Part of speech added successfully.")
        return



class CustomDictionary:
    def __init__(self):
        self.entries = {}

    def add_entry(self, word: str, definition: str, partOfSpeech: str, synonyms: List[str] = []):
        if word in self.word_entries:
            self.word_entries[word].add_definition(definition, partOfSpeech)
            self.word_entries[word].add_synonyms(synonyms)
        else:
            entry = DictionaryEntry(word, definition, synonyms, partOfSpeech)
            self.entries[word] = entry

    def get_entry(self, word: str):
        if word in self.entries:
            return self.entries[word]
        else:
            return None
        
    def get_synonyms(self, word: str):
        if word in self.entries:
            return self.entries[word].synonyms
        else:
            return None
    def get_definitions(self, word: str):
        if word in self.entries:
            return self.entries[word].definitions && self.entries[word].partOfSpeech
        else:
            return None
        
    
    def delete_entry(self, word: str):
        if word in self.entries:
            del self.entries[word]
            print("Entry deleted successfully.")
        else:
            print("Entry not found.")

    def get_all_entries(self):
        return self

    def update_entry(self, word: str, definition: str, partOfSpeech: str, synonyms: List[str] = []):
        if word in self.entries:
            self.entries[word].add_definition(definition, partOfSpeech)
            self.entries[word].add_synonyms(synonyms)
        else:
            print("Entry not found.")

    def save_dictionary(self):
        with open("dictionary_data.json", "w") as file:
            json.dump({"dictionary": self.dictionary, "synonyms": self.synonyms}, file)

    def load_dictionary(self):
        try:
            with open("dictionary_data.json", "r") as file:
                data = json.load(file)
                self.dictionary = data["dictionary"]
                self.synonyms = data["synonyms"]
        except FileNotFoundError:
            print("No saved dictionary found.")   