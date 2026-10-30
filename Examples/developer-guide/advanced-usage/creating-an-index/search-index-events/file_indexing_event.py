from groupdocs.search import Index
from groupdocs.search.common import DocumentField

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_file_indexing(sender, args):
    path = args.document_full_path.lower()
    if path.endswith("report.pdf"):
        args.additional_fields = [DocumentField("Tags", "Report")]
        print("Tagged:", args.document_full_path)
    if "important" in path:
        args.skip_indexing = True
        print("Skipped:", args.document_full_path)


index.events.file_indexing += on_file_indexing

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the added field
result = index.search("Tags:Report")
print("Documents found:", result.document_count)