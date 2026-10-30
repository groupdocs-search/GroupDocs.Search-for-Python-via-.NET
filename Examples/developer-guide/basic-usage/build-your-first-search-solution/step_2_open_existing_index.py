from groupdocs.search import Index

# Creating an index and indexing documents; the with statement releases the index
with Index("./index") as index:
    index.add("./documents")

# Loading the existing index from the same folder
index = Index("./index")
print("Indexed documents:", len(index.get_indexed_documents()))