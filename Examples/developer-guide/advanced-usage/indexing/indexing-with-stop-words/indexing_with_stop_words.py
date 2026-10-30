from groupdocs.search import Index, IndexSettings

# Creating index settings with the use of stop words disabled
settings = IndexSettings()
settings.use_stop_words = False

# Creating a new index in the specified folder
# The use_stop_words setting can be changed only while the index contains no documents
index = Index("./index", settings, True)

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
# Now in the index it is possible to search for the stop word 'on'
result = index.search("on")
print("Documents found:", result.document_count)