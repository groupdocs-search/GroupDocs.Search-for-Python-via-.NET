from groupdocs.search import Index

# Creating an in-memory index
index = Index()

# Indexing documents from the specified folder
index.add("./documents")

# Saving the index to disk
index.save_to("./index")

# Closing the in-memory index
index.dispose()

# Opening the index from disk
index = Index("./index")

# Searching in the index
query = "focus"
result = index.search(query)
print("Documents found:", result.document_count)