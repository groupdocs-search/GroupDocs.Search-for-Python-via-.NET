from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "Einstein AND NOT relativity"
result = index.search(query)
print("Documents found:", result.document_count)