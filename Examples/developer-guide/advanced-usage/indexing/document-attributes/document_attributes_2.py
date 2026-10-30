import os

from groupdocs.search import Index
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index
index = Index("./index")


# Subscribing to the file_indexing event for adding attributes
def on_file_indexing(sender, args):
    if args.document_full_path.endswith("KeyPoints.docx"):
        # Adding two attributes
        args.attributes = ["main", "key"]


index.events.file_indexing += on_file_indexing

# Indexing documents in a document folder
index.add("./documents")

# Searching in the index
options = SearchOptions()
# Creating a document filter by attribute
options.search_document_filter = SearchDocumentFilter.create_attribute("main")
result = index.search("Einstein", options)
for found in result:
    print("Found:", os.path.basename(found.document_info.file_path))