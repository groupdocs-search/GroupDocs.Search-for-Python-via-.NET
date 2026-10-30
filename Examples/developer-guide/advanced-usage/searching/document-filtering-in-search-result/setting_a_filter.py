import os

from groupdocs.search import Index
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options object
options = SearchOptions()
options.search_document_filter = SearchDocumentFilter.create_file_extension(".txt")  # Setting a document filter

# Search in the index
# Only text documents will be returned as the result of the search
result = index.search("relativity", options)

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))