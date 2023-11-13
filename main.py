import json

class CustomDictionary:
    def __init__(self):
        self.dictionary = {}
        self.synonyms = {}

    def add_word(self, word, part_of_speech, synonyms=None):
        if word not in self.dictionary:
            self.dictionary[word] = {"definitions": [], "synonyms": []}
        self.dictionary[word].append({"part_of_speech": part_of_speech, "definition": definition})
        if synonyms:
            self.dictionary[word]["synonyms"] = synonyms

            
    def add_synonyms(self, word, synonym_list):
        if word in self.dictionary:
            self.synonyms[word] = synonym_list
        else:
            print(f"Word '{word}' not found in dictionary.")

    def get_definitions(self, word):
        if word in self.dictionary:
            return [(entry["part_of_speech"], entry["definition"]) for entry in self.dictionary[word]]
        else:
            return "Word not found."

    def get_synonyms(self, word):
        return self.synonyms.get(word, [])

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

def main():
    my_dict = CustomDictionary()
    my_dict.load_dictionary()

    while True:
        command = input("Enter command (add, define, synonyms, save, quit): ").lower()
        if command == "add":
            word = input("Enter word: ")
            part_of_speech = input("Enter part of speech: ")
            definition = input("Enter definition: ")
            my_dict.add_word(word, part_of_speech, definition)
        elif command == "define":
            word = input("Enter word to define: ")
            definitions = my_dict.get_definitions(word)
            if isinstance(definitions, str):
                print(definitions)
            else:
                for part_of_speech, definition in definitions:
                    print(f"{part_of_speech}: {definition}")
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




