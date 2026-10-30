from groupdocs.search import Index
from groupdocs.search.options import UpdateOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Change, delete, add documents in the document folder
# ...

options = UpdateOptions()
options.threads = 2  # Setting the number of indexing threads
index.update(options)  # Updating the index

print("Indexed documents:", len(index.get_indexed_documents()))