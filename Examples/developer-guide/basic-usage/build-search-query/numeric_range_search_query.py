from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "2000 ~~ 3000"
result = index.search(query)  # Search for numbers from 2000 to 3000

# Printing the found numbers
for i in range(result.document_count):
    document = result.get_found_document(i)
    print(document.document_info.file_path, document.terms)