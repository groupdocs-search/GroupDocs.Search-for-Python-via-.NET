import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options object
options = SearchOptions()
options.use_homophone_search = True  # Enabling homophone search

# Search for the word 'coal'
# In addition to the word 'coal', the words 'cole' and 'kohl' will also be found
result = index.search("coal", options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)