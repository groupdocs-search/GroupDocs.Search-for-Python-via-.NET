import os

from groupdocs.search import Index, RegexOptions
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# The filter returns only files that contain the word 'Einstein' in their paths, not case sensitive
document_filter = SearchDocumentFilter.create_file_path_regular_expression("Einstein", RegexOptions.IGNORE_CASE)

# Search in the index with the filter
options = SearchOptions()
options.search_document_filter = document_filter
result = index.search("relativity", options)

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))