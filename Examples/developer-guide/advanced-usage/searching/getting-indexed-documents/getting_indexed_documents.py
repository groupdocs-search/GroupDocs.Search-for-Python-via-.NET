from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Getting list of indexed documents
documents = index.get_indexed_documents()
for document in documents:
    print(document.file_path)
    items = index.get_indexed_document_items(document)  # Getting list of document items
    for item in items:
        print("\t" + item.inner_path)