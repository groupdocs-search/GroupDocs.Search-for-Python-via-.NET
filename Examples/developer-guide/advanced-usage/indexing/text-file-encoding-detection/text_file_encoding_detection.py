from groupdocs.search import Index
from groupdocs.search.common import Encodings

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_file_indexing(sender, args):
    if args.document_full_path.lower().endswith(".txt"):
        args.encoding = Encodings.WINDOWS_1253  # Setting encoding for each text file


index.events.file_indexing += on_file_indexing

# Indexing documents from the specified folder
index.add("./documents")

# Searching for a Greek word ("relativity")
result = index.search("σχετικότητας")
print("Documents found:", result.document_count)