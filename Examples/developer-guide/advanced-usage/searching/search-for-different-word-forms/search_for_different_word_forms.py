import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options instance
options = SearchOptions()
options.use_word_forms_search = True  # Enabling search for word forms

# Searching in the index
result = index.search("relative", options)

# The following words can be found:
# relative
# relatives
# relatively

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)