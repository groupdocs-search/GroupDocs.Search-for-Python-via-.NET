from groupdocs.search import Index

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_password_required(sender, args):
    if args.document_full_path.lower().endswith("protected.pdf"):
        args.password = "123456"
        print("Password supplied for:", args.document_full_path)


index.events.password_required += on_password_required

# Indexing documents from the specified folder
index.add("./documents")

# Searching for a word of the protected document
result = index.search("confidential")
print("Documents found:", result.document_count)