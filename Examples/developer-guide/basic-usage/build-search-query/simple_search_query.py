from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "Einstein"
result = index.search(query)  # Search in the index
print("Documents found:", result.document_count)