from groupdocs.search import Index
from groupdocs.search.options import NumberOfThreads

# Creating an index, indexing documents and closing the index
index = Index("./index")
index.add("./documents")
index.dispose()

# Opening the existing index
index = Index("./index")

# Changing the number of threads used for the search; the new value is saved in the index
index.index_settings.search_threads = NumberOfThreads.ONE

# Searching using the new number of threads
result = index.search("Einstein")
print("Documents found:", result.document_count)