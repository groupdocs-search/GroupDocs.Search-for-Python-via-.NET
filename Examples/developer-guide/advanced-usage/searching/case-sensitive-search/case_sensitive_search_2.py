import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import SearchOptions

index = Index("./index")  # Creating index in the specified folder
index.add("./documents")  # Indexing documents from the specified folder

options = SearchOptions()
options.use_case_sensitive_search = True  # Enabling case sensitive search

query = SearchQuery.create_word_query("Windows")  # Creating search query in object form

result = index.search(query, options)  # Searching

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)