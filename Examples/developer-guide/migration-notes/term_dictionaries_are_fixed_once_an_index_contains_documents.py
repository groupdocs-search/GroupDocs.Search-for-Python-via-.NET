from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType

# Creating a new index; an existing index in the folder is overwritten
index = Index("./index", True)

# Configuring the term dictionaries while the index contains no documents
index.dictionaries.alphabet.set_range(["-"], CharacterType.BLENDED)
index.dictionaries.stop_word_dictionary.add_range(["and", "or", "the"])

# Indexing documents; after this, the dictionaries above cannot be changed
index.add("./documents")
print("Indexed documents:", len(index.get_indexed_documents()))