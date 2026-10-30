from groupdocs.search import Index

index = Index("./index")
index.add("./documents")

query = "FileName: relativ?(1~3) OR Content: (Einstein AND Albert)"
result = index.search(query)  # Search for documents whose file names contain 'relative', 'relativity', etc., or documents containing both 'Einstein' and 'Albert' in the content
print("Documents found:", result.document_count)