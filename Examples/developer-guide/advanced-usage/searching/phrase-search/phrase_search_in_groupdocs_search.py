import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search for the phrase 'theory of relativity' in text form
query1 = '"theory of relativity"'
result1 = index.search(query1)

# Search for the phrase 'theory of relativity' in object form
word1 = SearchQuery.create_word_query("theory")
word2 = SearchQuery.create_word_query("of")
word3 = SearchQuery.create_word_query("relativity")
query2 = SearchQuery.create_phrase_search_query(word1, word2, word3)
result2 = index.search(query2)

# Printing the documents found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path))