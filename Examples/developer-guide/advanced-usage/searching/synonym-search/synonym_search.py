import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options object
options = SearchOptions()
options.use_synonym_search = True  # Enabling synonym search

# Search for the word 'answer'
# In addition to the word 'answer', the words 'reply' and 'response' will also be found
result = index.search("answer", options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)