import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder one by one, so that each document gets its own index segment
for file_name in sorted(os.listdir("./documents")):
    index.add(os.path.join("./documents", file_name))
print("Index segments: " + str(index.index_info.segment_count))

# Creating a search options instance
options = SearchOptions()
options.is_chunk_search = True  # Enabling the search by chunks

# Starting the search by chunks
result = index.search(query, options)
print("Document count: " + str(result.document_count))
print("Occurrence count: " + str(result.occurrence_count))

# Continuing the search by chunks while there are chunks left
while result.next_chunk_search_token is not None:
    result = index.search_next(result.next_chunk_search_token)
    print("Document count: " + str(result.document_count))
    print("Occurrence count: " + str(result.occurrence_count))