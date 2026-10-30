from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "Einstein"  # Specify a search query

# Search in index
result = index.search(query)

# Printing the result
print("Documents found:", result.document_count)
print("Total occurrences found:", result.occurrence_count)
for i in range(result.document_count):
    document = result.get_found_document(i)
    print("\tDocument:", document.document_info.file_path)
    print("\tOccurrences:", document.occurrence_count)