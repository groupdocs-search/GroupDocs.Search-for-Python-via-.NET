from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index in the specified folder
index = Index("./index", True)

# Setting the separate word type for the CJK unified ideographs
characters = [chr(code_point) for code_point in range(0x4E00, 0x9FFF + 1)]
index.dictionaries.alphabet.set_range(characters, CharacterType.SEPARATE_WORD)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index for a single character
result = index.search("书")
print("Documents found:", result.document_count)
print("Occurrences found:", result.occurrence_count)