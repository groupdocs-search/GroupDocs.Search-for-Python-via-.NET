import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options object
options = SearchOptions()
options.keyboard_layout_corrector.enabled = True  # Enabling keyboard layout correction

# Search for the word 'Уштыеушт' gives documents containing the word 'Einstein'
result = index.search("Уштыеушт", options)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)