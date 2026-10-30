import os

from groupdocs.search import Index
from groupdocs.search.common import Cancellation
from groupdocs.search.options import SearchOptions

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder one by one, so that each document gets its own index segment
for file_name in sorted(os.listdir("./documents")):
    index.add(os.path.join("./documents", file_name))

# Creating a cancellation object that cancels the search after 10 seconds
cancellation = Cancellation()
cancellation.cancel_after(10000)

# Creating a search options instance
options = SearchOptions()
options.is_chunk_search = True  # Enabling the search by chunks
options.cancellation = cancellation  # Cancellation of the first chunk

# Starting the search by chunks
result = index.search(query, options)
print("Document count: " + str(result.document_count))

# Continuing the search by chunks until the search is complete or canceled
while result.next_chunk_search_token is not None and not cancellation.is_cancelled:
    result = index.search_next(result.next_chunk_search_token, cancellation)
    print("Document count: " + str(result.document_count))