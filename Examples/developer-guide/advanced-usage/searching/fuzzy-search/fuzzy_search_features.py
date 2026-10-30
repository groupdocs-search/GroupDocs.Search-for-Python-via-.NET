import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions, SimilarityLevel

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

options = SearchOptions()
options.fuzzy_search.enabled = True  # Enabling the fuzzy search
options.fuzzy_search.fuzzy_algorithm = SimilarityLevel(0.75)  # Creating the fuzzy search algorithm
# This function specifies 0 as the maximum number of mistakes for words from 1 to 3 characters.
# It specifies 1 as the maximum number of mistakes for words from 4 to 7 characters.
# It specifies 2 as the maximum number of mistakes for words from 8 to 11 characters. And so on.

# Search in index
result = index.search(query, options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)