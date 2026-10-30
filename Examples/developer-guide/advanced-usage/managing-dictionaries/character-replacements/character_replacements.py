from groupdocs.search import Index, IndexSettings
from groupdocs.search.dictionaries import CharacterReplacementPair

# Creating an index settings instance
settings = IndexSettings()
settings.use_character_replacements = True  # Enabling character replacements during indexing

# Creating a new index in the specified folder; the dictionary can be changed only while the index contains no documents
index = Index("./index", settings, True)

replacements = index.dictionaries.character_replacements

if replacements.contains(ord("-")):
    # Getting the replacement for the hyphen character
    replacement = replacements.get_replacement(ord("-"))
    print("The replacement for hyphen is " + chr(replacement))

    # Deleting the hyphen character replacement from the dictionary
    replacements.remove_range(["-"])

if replacements.count > 0:
    # Deleting all character replacements from the dictionary
    replacements.clear()

# Adding character replacements to the dictionary
pairs = [
    CharacterReplacementPair("Ä", "a"),
    CharacterReplacementPair("ä", "a"),
    CharacterReplacementPair(0x1D400, 0x0061),  # Mathematical bold capital A is replaced with the small letter a
]
replacements.add_range(pairs)

# Exporting character replacements to a file
replacements.export_dictionary("./CharacterReplacements.dat")

# Importing character replacements from a file
replacements.import_dictionary("./CharacterReplacements.dat")
print("Character replacements:", replacements.count)
print("The replacement for Ä is " + chr(replacements.get_replacement(ord("Ä"))))

# Indexing documents; after that, the character replacements of the index cannot be changed
index.add("./documents")