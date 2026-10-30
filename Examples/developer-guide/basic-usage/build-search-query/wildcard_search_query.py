from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "?ffect"
result = index.search(query)  # Search for words 'affect', 'effect', etc.

# Printing the found words
for i in range(result.document_count):
    document = result.get_found_document(i)
    print(document.document_info.file_path, document.terms)