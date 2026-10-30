from groupdocs.search import Index, IndexSettings
from groupdocs.search.options import IndexType

# Creating an instance of index settings
settings = IndexSettings()
settings.index_type = IndexType.METADATA_INDEX  # Setting index type

# Creating a new index in the specified folder
index = Index("./index", settings, True)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
result = index.search("Einstein")
print("Documents found:", result.document_count)