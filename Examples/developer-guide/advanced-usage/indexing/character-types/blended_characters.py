from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index in the specified folder
index = Index("./index", True)

# Setting hyphen character type to blended
index.dictionaries.alphabet.set_range(["-"], CharacterType.BLENDED)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
result1 = index.search("Elliot-Murray-Kynynmound")
result2 = index.search("Elliot")
result3 = index.search("Murray")
result4 = index.search("Kynynmound")
for query, result in [("Elliot-Murray-Kynynmound", result1), ("Elliot", result2),
                      ("Murray", result3), ("Kynynmound", result4)]:
    print(query + ":", result.document_count, "document(s)")