from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = r"^(.)\1{2,}"  # The caret character at the beginning indicates that this is a regular expression search query
result = index.search(query)  # Search for three or more identical characters in a row

# Printing the found words
for i in range(result.document_count):
    document = result.get_found_document(i)
    print(document.document_info.file_path, document.terms)