from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import FileLogger

# Creating a regular index on disk
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Closing the regular index
index.dispose()

# Loading the index entirely in memory for increased performance
# The logger is not saved in the index, so it is passed with the settings
settings = IndexSettings()
settings.logger = FileLogger("./log.txt", 4.0)
in_memory_index = Index.load_into_memory_completely("./index", settings)

# Searching in the index
query = "focus"
result = in_memory_index.search(query)
print("Documents found:", result.document_count)