import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with a regular expression in text form
query1 = "^^(.)\\1{1,}"  # The first caret character at the beginning indicates that this is a regular expression search query
result1 = index.search(query1)  # Search for two or more identical characters at the beginning of a word

# Search with a regular expression in object form
query2 = SearchQuery.create_regex_query("^(.)\\1{1,}")  # Search for two or more identical characters at the beginning of a word
result2 = index.search(query2)

# Printing the words found in each document
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)