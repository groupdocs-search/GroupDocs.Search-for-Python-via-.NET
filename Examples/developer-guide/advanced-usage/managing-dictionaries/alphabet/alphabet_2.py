from groupdocs.search import Index

# Creating a new index in the specified folder
new_index = Index("./new-index", True)

# Setting the Separator type for all characters, so that only the imported types remain in the alphabet
new_index.dictionaries.alphabet.clear()

# Importing the alphabet from a file
new_index.dictionaries.alphabet.import_dictionary("./Alphabet.dat")
print("Characters that are not separators:", new_index.dictionaries.alphabet.count)

# Indexing documents
new_index.add("./documents")