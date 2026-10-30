import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with object query combining three words with the AND operator
and_query = SearchQuery.create_and_query(
    SearchQuery.create_word_query("theory"),
    SearchQuery.create_word_query("special"),
    SearchQuery.create_word_query("relativity"))
result = index.search(and_query)

# Printing the documents found
print("Query:", and_query.to_string())
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))