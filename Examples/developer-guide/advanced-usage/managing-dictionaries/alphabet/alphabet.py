from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index in the specified folder; the alphabet can be changed only while the index contains no documents
index = Index("./index", True)

alphabet = index.dictionaries.alphabet

# Getting the type of the hyphen character
hyphen_type = alphabet.get_character_type("-")
print("The type of hyphen:", hyphen_type.name)

if hyphen_type != CharacterType.BLENDED:
    # Setting the Blended type for the hyphen character
    alphabet.set_range(["-"], CharacterType.BLENDED)

# Setting the Letter type for characters outside the Basic Multilingual Plane specified as Unicode code points
alphabet.set_range([0x1D400, 0x1D401], CharacterType.LETTER)  # Mathematical bold capital A and B

# Setting the Letter type for a character outside the Basic Multilingual Plane specified as a string
alphabet.set_range(["\U0001D41A"], CharacterType.LETTER)  # Mathematical bold small A

# Getting the types of characters specified as a Unicode code point and as a string
print("The type of U+1D400:", alphabet.get_character_type(0x1D400).name)
print("The type of U+1D41A:", alphabet.get_character_type("\U0001D41A").name)

# Getting the number of characters that are not separators
print("Characters that are not separators:", alphabet.count)

# Exporting the alphabet to a file
alphabet.export_dictionary("./Alphabet.dat")

# Indexing documents; after that, the alphabet of the index cannot be changed
index.add("./documents")