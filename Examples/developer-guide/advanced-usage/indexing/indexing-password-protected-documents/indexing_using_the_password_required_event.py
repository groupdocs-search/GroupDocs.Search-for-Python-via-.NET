from groupdocs.search import Index

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_password_required(sender, args):
    if args.document_full_path.lower().endswith("protecteddocument.docx"):
        args.password = "123456"  # Providing password for the file 'ProtectedDocument.docx'


index.events.password_required += on_password_required

# Indexing documents from the specified folder
index.add("./documents")

result = index.search("strikethrough")
print("Documents found:", result.document_count)