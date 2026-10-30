from groupdocs.search import Index

# Creating a new index in the specified folder
new_index = Index("./new-index", True)

# Setting the Separator type for all characters, so that only the imported types remain in the dictionary
new_index.dictionaries.tokenization_dictionary.clear()

# Importing the tokenization dictionary from a file
new_index.dictionaries.tokenization_dictionary.import_dictionary("./TokenizationDictionary.dat")
print("Characters that are not separators:", new_index.dictionaries.tokenization_dictionary.count)