import os

from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Getting an indexed document by its file path
document = index.get_indexed_document(os.path.abspath("./documents/einstein-biography.txt"))
if document is not None:
    print(document.file_path + " (" + str(document.file_type) + ")")