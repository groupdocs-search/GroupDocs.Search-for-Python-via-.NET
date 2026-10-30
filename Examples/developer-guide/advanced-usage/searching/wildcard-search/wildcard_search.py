import os

from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search in the index
result1 = index.search("m?rry")  # Search for 'merry', 'marry', etc.
result2 = index.search("card?(1~6)")  # Search for 'cardiff', 'cardinal', 'cardio', 'cards', etc.

# Printing the words found
for query, result in (("m?rry", result1), ("card?(1~6)", result2)):
    print(query, "- documents found:", result.document_count)
    for document in result:
        print("   ", os.path.basename(document.document_info.file_path), document.terms)