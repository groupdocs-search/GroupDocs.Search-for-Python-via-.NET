import os

from groupdocs.search import Index, RegexOptions
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating an AND composite filter that returns all FB2 and EPUB documents that have the word 'Einstein' in their full paths
filter1 = SearchDocumentFilter.create_file_path_regular_expression("Einstein", RegexOptions.IGNORE_CASE)
filter2 = SearchDocumentFilter.create_file_extension(".fb2", ".epub")
and_filter = SearchDocumentFilter.create_and(filter1, filter2)

# Creating an OR composite filter that returns all DOC, DOCX, PDF and all documents that have the word Einstein in their full paths
filter3 = SearchDocumentFilter.create_file_path_regular_expression("Einstein", RegexOptions.IGNORE_CASE)
filter4 = SearchDocumentFilter.create_file_extension(".doc", ".docx", ".pdf")
or_filter = SearchDocumentFilter.create_or(filter3, filter4)

# Creating a filter that returns all found documents except TXT documents
filter5 = SearchDocumentFilter.create_file_extension(".txt")
not_filter = SearchDocumentFilter.create_not(filter5)

# Searching with each of the composite filters
for document_filter in (and_filter, or_filter, not_filter):
    options = SearchOptions()
    options.search_document_filter = document_filter
    result = index.search("relativity", options)
    print(document_filter, "- documents found:", result.document_count)
    for document in result:
        print("   ", os.path.basename(document.document_info.file_path))