from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "Content: Einstein"
result = index.search(query)  # Search for word 'Einstein' only in 'Content' field
print("Documents found:", result.document_count)