from groupdocs.search import Index, IndexSettings
from groupdocs.search.dictionaries import CharacterReplacementPair

# Enabling character replacements in the index settings
settings = IndexSettings()
settings.use_character_replacements = True

# Creating a new index in the specified folder
# The character replacements can be changed only while the index contains no documents
index = Index("./index", settings, True)

# Configuring character replacements
# Deleting all existing character replacements from the dictionary
index.dictionaries.character_replacements.clear()
# Creating new character replacements: each character is replaced with its lowercase form
character_replacements = []
for code_point in range(0x10000):
    character = chr(code_point)
    replacement = character.lower()
    # A character that does not change needs no replacement
    if replacement != character and len(replacement) == 1:
        character_replacements.append(CharacterReplacementPair(character, replacement))
# Adding character replacements to the dictionary
index.dictionaries.character_replacements.add_range(character_replacements)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
# Case-sensitive search is no longer possible for this index, since all characters are lowercase
# By default, case-insensitive search is performed
result = index.search("Einstein")
print("Documents found:", result.document_count)