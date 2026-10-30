import os

from groupdocs.search import Index
from groupdocs.search.common import AttributeChangeBatch
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index
index = Index("./index")

# Indexing documents in a document folder
index.add("./documents")

# The full path of a document identifies it in the index
key_points = os.path.abspath("./documents/KeyPoints.docx")

# Creating an attribute change container object
batch = AttributeChangeBatch()
# Adding one attribute to all indexed documents
batch.add_to_all(["public"])
# Removing one attribute from one indexed document
batch.remove(key_points, ["public"])
# Adding two attributes to one indexed document
batch.add(key_points, ["main", "key"])

# Applying attribute changes in the index
index.change_attributes(batch)

# Searching in the index
options = SearchOptions()
# Creating a document filter by attribute
options.search_document_filter = SearchDocumentFilter.create_attribute("main")
result = index.search("Einstein", options)
for found in result:
    print("Found:", os.path.basename(found.document_info.file_path))
print("Attributes of KeyPoints.docx:", ", ".join(index.get_attributes(key_points)))