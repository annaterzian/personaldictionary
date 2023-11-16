import json

class WordEntry:
    def __init__(self, word='', definition='', synonyms=[], part=''):
        self.word = word
        self.definition = definition
        self.synonyms = synonyms
        self.part = part

    def add_def(self, part, definition):
        self.definitions.append({'Part of Speech': part, 'definition': definition})

    def add_synonyms(self, synonyms):
        self.synonyms.extend(synonyms)

    def __str__(self):
        definitions_str = '\n'.join(
            f'{d['Part of Speech']}: {d['definition']}' for d in self.definitions
        )
        synonyms_str = ', '.join(self.synonyms)
        return f'{self.word}\nDefinitions:\n{definitions_str}\nSynonyms:'

class CustomDictionary:
    def __init__(self):
        self.entries = {}

    def add_word(self, word, definition, synonyms, part):
        if word not in self.entries:
            self.entries[word] = WordEntry(word, definition, synonyms, part)

    def add_def(self, word, part, definition):
        if word in self.entries:
            self.entries[word].add_definition(part, definition)
        else:
            print(f"Word '{word}' not found in dictionary.")
    
    def add_synonyms(self, word, synonyms):
        if word in self.entries:
            self.entries[word].add_synonyms(synonyms)
        else:
            print(f"Word '{word}' not found in dictionary.")

    def find_word_entry(self, word):
        return self.entries.get(word)

    def __str__(self):
        return "\n".join(str(entry) for entry in self.entries.values())

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

# class CustomDictionary:
#     def __init__(self):
#         self.dictionary = {}
#         self.synonyms = {}

#     def add_word(self, word, part_of_speech, definition, synonyms=None):
#         if word not in self.dictionary:
#             self.dictionary[word] = {"definitions": [], "synonyms": []}
#         self.dictionary[word].append({"part_of_speech": part_of_speech, "definition": definition})
#         if synonyms:
#             self.dictionary[word]["synonyms"] = synonyms

            
#     def add_synonyms(self, word, synonym_list):
#         if word in self.dictionary:
#             self.synonyms[word] = synonym_list
#         else:
#             print(f"Word '{word}' not found in dictionary.")

#     def get_definitions(self, word):
#         if word in self.dictionary:
#             return [(entry["part_of_speech"], entry["definition"]) for entry in self.dictionary[word]]
#         else:
#             return "Word not found."

#     def get_synonyms(self, word):
#         return self.synonyms.get(word, [])

#     def save_dictionary(self):
#         with open("dictionary_data.json", "w") as file:
#             json.dump({"dictionary": self.dictionary, "synonyms": self.synonyms}, file)

#     def load_dictionary(self):
#         try:
#             with open("dictionary_data.json", "r") as file:
#                 data = json.load(file)
#                 self.dictionary = data["dictionary"]
#                 self.synonyms = data["synonyms"]
#         except FileNotFoundError:
#             print("No saved dictionary found.")

def main():
    my_dict = CustomDictionary()
    my_dict.load_dictionary()

    while True:
        command = input("Enter command (add, define, synonyms, save, quit): ").lower()
        if command == "add":
            word = input("Enter word: ")
            part = input("Enter part of speech: ")
            definition = input("Enter definition: ")
            my_dict.add_word(word, definition, [], part)
        elif command == "define":
            word = input("Enter word to define: ")
            definitions = my_dict.get_definitions(word)
            if isinstance(definitions, str):
                print(definitions)
            else:
                for part, definition in definitions:
                    print(f"{part}: {definition}")
        elif command == "synonyms":
            word = input("Enter word to find synonyms: ")
            synonyms = input("Enter synonyms separated by commas: ").split(',')
            my_dict.add_synonyms(word, synonyms)
        elif command == "save":
            my_dict.save_dictionary()
            print("Dictionary saved.")
        elif command == "quit":
            break

if __name__ == "__main__":
    main()




