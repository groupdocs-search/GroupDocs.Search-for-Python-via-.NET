from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# Creating an index in the specified folder
index = Index("./index")

# Creating an instance of indexing options
options = IndexingOptions()
options.threads = 2  # Setting the number of indexing threads

# Indexing documents from the specified folder
index.add("./documents", options)

print("Indexed documents:", len(index.get_indexed_documents()))