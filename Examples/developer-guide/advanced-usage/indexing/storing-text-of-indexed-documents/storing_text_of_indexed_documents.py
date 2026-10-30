from groupdocs.search import Index, IndexSettings
from groupdocs.search.options import Compression, TextStorageSettings

# Creating an index settings instance
settings = IndexSettings()
settings.text_storage_settings = TextStorageSettings(Compression.HIGH)  # Setting high compression ratio for the index text storage

# Creating a new index in the specified folder
index = Index("./index", settings, True)

# Indexing documents
index.add("./documents")

# Searching
result = index.search("Einstein")
print("Documents found:", result.document_count)