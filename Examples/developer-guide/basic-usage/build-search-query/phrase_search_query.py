from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = '"theory of special relativity"'
result = index.search(query)  # Search for the phrase 'theory of special relativity'
print("Documents found:", result.document_count)