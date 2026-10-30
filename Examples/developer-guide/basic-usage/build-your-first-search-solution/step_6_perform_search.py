from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "Einstein"  # Specify a search query
result = index.search(query)  # Searching in the index
print("Documents found:", result.document_count)