import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options instance
options = SearchOptions()
options.spelling_corrector.enabled = True  # Enabling the spelling correction
options.spelling_corrector.max_mistake_count = 1  # Setting the maximum number of mistakes
options.spelling_corrector.only_best_results = True  # Enabling the option for only the best results of the spelling correction

# Search for the word "Rleativity" containing a spelling error
# The word "Relativity" will be found that differs from the search query in two transposed letters
result = index.search("Rleativity", options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)