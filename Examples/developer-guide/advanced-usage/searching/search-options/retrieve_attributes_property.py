import os

from groupdocs.search import Index
from groupdocs.search.common import AttributeChangeBatch
from groupdocs.search.options import SearchOptions

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Associating attributes with one of the indexed documents (see the Document attributes page)
batch = AttributeChangeBatch()
batch.add(os.path.abspath("./documents/einstein-biography.txt"), ["main", "biography"])
index.change_attributes(batch)

# Creating a search options instance
options = SearchOptions()
options.retrieve_attributes = True  # Enabling the retrieval of document attributes

# Search in the index
result = index.search(query, options)

# Printing the attributes of the found documents
for i in range(result.document_count):
    document = result.get_found_document(i)
    print(document.document_info.file_path + ": " + ", ".join(document.attributes))