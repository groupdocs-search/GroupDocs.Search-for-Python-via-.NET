import os

from groupdocs.search import Index

# Creating an index
index = Index("./index")

# Adding document passwords to the dictionary
# (an index opened again keeps its dictionary, so the password may be there already)
key = os.path.abspath("./documents/ProtectedDocument.docx")
if not index.dictionaries.document_passwords.contains(key):
    index.dictionaries.document_passwords.add(key, "123456")
# ...

# Indexing documents from the specified folder
# Passwords will be automatically retrieved from the dictionary when necessary
index.add("./documents")

result = index.search("strikethrough")
print("Documents found:", result.document_count)