from groupdocs.search import Index

try:
    import chardet  # pip install chardet
except ImportError:
    chardet = None

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_file_indexing(sender, args):
    if args.document_full_path is not None and args.document_full_path.lower().endswith(".txt"):
        if chardet is None:
            print("chardet is not installed: the default encoding is used")
            return
        with open(args.document_full_path, "rb") as f:
            data = f.read()
        result = chardet.detect(data)
        if result["encoding"] is not None:
            print("Encoding detected: " + result["encoding"])
            args.encoding = result["encoding"]


index.events.file_indexing += on_file_indexing

# Indexing documents from the specified folder
index.add("./documents")