import os

from groupdocs.search import Index
from groupdocs.search.common import AttributeChangeBatch
from groupdocs.search.options import SearchDocumentFilter, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Associating the attribute "main" with one of the indexed documents
batch = AttributeChangeBatch()
batch.add(os.path.abspath("./documents/relativity-lecture.pdf"), ["main"])
index.change_attributes(batch)

# This filter returns only documents that have attribute "main"
document_filter = SearchDocumentFilter.create_attribute("main")

# Search in the index with the filter
options = SearchOptions()
options.search_document_filter = document_filter
result = index.search("relativity", options)

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))