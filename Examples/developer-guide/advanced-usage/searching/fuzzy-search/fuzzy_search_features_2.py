import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions, Step, TableDiscreteFunction

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

options = SearchOptions()
options.fuzzy_search.enabled = True  # Enabling the fuzzy search
options.fuzzy_search.fuzzy_algorithm = TableDiscreteFunction(1, [Step(5, 2), Step(8, 3)])  # Creating the fuzzy search algorithm
# This function specifies 1 as the maximum number of mistakes for words from 1 to 4 characters.
# It specifies 2 as the maximum number of mistakes for words from 5 to 7 characters.
# It specifies 3 as the maximum number of mistakes for words from 8 and more characters.

# Search in index
result = index.search(query, options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)