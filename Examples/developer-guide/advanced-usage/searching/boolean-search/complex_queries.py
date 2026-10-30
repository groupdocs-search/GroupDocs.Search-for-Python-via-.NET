import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with text query
result1 = index.search("(theory AND relativity) AND NOT (Einstein OR Albert)")

# Search with object query
theory_word_query = SearchQuery.create_word_query("theory")
relativity_word_query = SearchQuery.create_word_query("relativity")
and_query = SearchQuery.create_and_query(theory_word_query, relativity_word_query)

einstein_word_query = SearchQuery.create_word_query("Einstein")
albert_word_query = SearchQuery.create_word_query("Albert")
or_query = SearchQuery.create_or_query(einstein_word_query, albert_word_query)
not_query = SearchQuery.create_not_query(or_query)

root_query = SearchQuery.create_and_query(and_query, not_query)
result2 = index.search(root_query)

# Printing the documents found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path))