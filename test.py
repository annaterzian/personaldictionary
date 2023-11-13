# import argparse
# import json

# dictionary = {
#     "word": {
#         "definition": "definition text",
#         "part_of_speech": "noun/verb/adjective/etc."
#         "synonyms": ["synonym1", "synonym2"]
#     }
# }

# def add_word(word, definition, part_of_speech, synonyms):
#     #add new word to dictionary
#     pass

# def find_word(word):
#     #retrieve a word's definition and synonyms
#     pass

# def update_word(word):
#     #update a word's definition and synonyms
#     pass

# def delete_word(word):
#     #delete word from dictionary
#     pass

# def saveDictionary(dictionary):
#     #saves entire dictionary
#     pass

# def loadDictionary(dictionary):
#     #loads specific dictionary
#     pass


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Custom Dictionary CLI")
#     #set up argparse commands

#     args = parser.parse_args()

#     #CLI logic implementation


# class TrieNode:
    
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end_of_word

