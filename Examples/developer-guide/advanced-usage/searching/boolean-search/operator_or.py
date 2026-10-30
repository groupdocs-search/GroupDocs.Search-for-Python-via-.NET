import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with text query
result1 = index.search("Einstein OR relativity")

# Search with object query
word_query1 = SearchQuery.create_word_query("Einstein")
word_query2 = SearchQuery.create_word_query("relativity")
or_query = SearchQuery.create_or_query(word_query1, word_query2)
result2 = index.search(or_query)

# Printing the documents found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)