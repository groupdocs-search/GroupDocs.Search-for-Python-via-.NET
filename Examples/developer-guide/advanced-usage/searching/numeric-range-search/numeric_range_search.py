import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with text query
result1 = index.search("500 ~~ 600")

# Search with object query
query2 = SearchQuery.create_numeric_range_query(500, 600)
result2 = index.search(query2)

# Printing the numbers found in each document
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)