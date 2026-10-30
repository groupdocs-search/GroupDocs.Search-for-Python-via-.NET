from groupdocs.search import Index

# Creating or opening an index in the specified folder
index = Index("./index")

corrector = index.dictionaries.spelling_corrector

if corrector.count > 0:
    # Removing all words from the dictionary
    corrector.clear()

# Adding words to the dictionary
words = ["achieve", "accomplish", "attain", "reach"]
corrector.add_range(words)

# Getting all words of the dictionary
all_words = corrector.get_words()
print("Words in the dictionary:", len(all_words))

# Exporting words to a file
corrector.export_dictionary("./Words.txt")

# Importing words from a file
corrector.import_dictionary("./Words.txt")