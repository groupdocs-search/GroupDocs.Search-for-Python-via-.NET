from groupdocs.search import Index

index = Index("./index")  # Creating an index in the specified folder
index.add("./documents")  # Indexing documents from the specified folder
print("Indexed documents:", len(index.get_indexed_documents()))