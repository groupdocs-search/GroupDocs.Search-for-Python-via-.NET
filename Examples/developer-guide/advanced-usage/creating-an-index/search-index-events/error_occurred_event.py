from groupdocs.search import Index

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_error_occurred(sender, args):
    # Writing an error message to the console
    print(("Critical error: " if args.is_critical else "Error: ") + args.message)


index.events.error_occurred += on_error_occurred

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the index
result = index.search("Einstein")
print("Documents found:", result.document_count)