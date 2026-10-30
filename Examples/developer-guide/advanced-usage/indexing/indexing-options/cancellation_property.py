from groupdocs.search import Index
from groupdocs.search.common import Cancellation
from groupdocs.search.options import IndexingOptions

# Creating an index in the specified folder
index = Index("./index")

# Creating an instance of indexing options
options = IndexingOptions()
options.cancellation = Cancellation()  # Setting a cancellation object
options.cancellation.cancel_after(300000)  # Setting a time period of 300 seconds after which the indexing operation will be cancelled

# Indexing documents from the specified folder
index.add("./documents", options)

print("Indexed documents:", len(index.get_indexed_documents()))