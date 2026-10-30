from groupdocs.search import Index

# Creating or opening an index in the specified folder
index = Index("./index")

synonyms = index.dictionaries.synonym_dictionary

# Getting synonyms for the word 'make'; the letter case of the word is ignored
words = synonyms.get_synonyms("Make")
print("Synonyms for 'make':")
for word in words:
    print(word)

# Getting groups of synonyms to which the word 'make' belongs
groups = synonyms.get_synonym_groups("make")
print("Synonym groups for 'make':")
for group in groups:
    print(" ".join(group))

if synonyms.count > 0:
    # Removing all synonyms from the dictionary
    synonyms.clear()

# Adding synonyms to the dictionary
synonym_groups = [
    ["achieve", "accomplish", "attain", "reach"],
    ["accept", "take", "have"],
]
synonyms.add_range(synonym_groups)
print("Words in the dictionary:", synonyms.count)

# Exporting synonyms to a file
synonyms.export_dictionary("./Synonyms.dat")

# Importing synonyms from a file
synonyms.import_dictionary("./Synonyms.dat")