from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index in the specified folder
# The alphabet can be changed only while the index contains no documents
index = Index("./index", True)

# Configuring the alphabet
# Setting the separator type for all characters in the alphabet
index.dictionaries.alphabet.clear()
# Creating a list of letter characters
characters = []
for code_point in range(0x0030, 0x0039 + 1):
    characters.append(chr(code_point))  # Digits
for code_point in range(0x0041, 0x005A + 1):
    characters.append(chr(code_point))  # Latin capital letters
characters.append(chr(0x005F))  # Low line
for code_point in range(0x0061, 0x007A + 1):
    characters.append(chr(code_point))  # Latin small letters
# Setting the type of characters in the alphabet
index.dictionaries.alphabet.set_range(characters, CharacterType.LETTER)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
result = index.search("Einstein")
print("Documents found:", result.document_count)