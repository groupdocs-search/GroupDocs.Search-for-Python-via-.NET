import os

from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Adding aliases to the alias dictionary
index.dictionaries.alias_dictionary.add("t", "(theory OR relativity)")
index.dictionaries.alias_dictionary.add("e", "(Einstein OR Albert)")

# Search in the index
result = index.search("@t OR @e")

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)