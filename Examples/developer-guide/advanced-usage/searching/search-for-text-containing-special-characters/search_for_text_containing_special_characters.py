import os

from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index in the specified folder (the existing index files are deleted)
index = Index("./index", True)

# Setting character types before indexing documents
index.dictionaries.alphabet.set_range(["&"], CharacterType.LETTER)
index.dictionaries.alphabet.set_range(["-"], CharacterType.SEPARATOR)

# Indexing documents from the specified folder
index.add("./documents")

# Defining a search query
word = "rock&roll-music"

# Replacing separators with the space characters
result = []
for character in word:
    character_type = index.dictionaries.alphabet.get_character_type(character)
    if character_type == CharacterType.SEPARATOR:
        result.append(" ")
    else:
        result.append(character)

# Escaping special characters
special_characters = "():\"&|!^~*?\\"
for i in range(len(result) - 1, -1, -1):
    if result[i] in special_characters:
        result.insert(i, "\\")

query = "".join(result)
if " " in query:
    query = "\"" + query + "\""

# Searching
search_result = index.search(query)

# Printing the query and the documents found
print("Query:", query)
print("Documents found:", search_result.document_count)
for document in search_result:
    print("   ", os.path.basename(document.document_info.file_path))