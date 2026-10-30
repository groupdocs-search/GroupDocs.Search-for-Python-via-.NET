import datetime

from groupdocs.search import Index
from groupdocs.search.common import Document
from groupdocs.search.options import IndexingOptions

document_file_path = "./sample.pdf"

# Creating an index
index = Index("./index")

# Creating a document object
stream = open(document_file_path, "rb")  # Opening a stream
document = Document.create_from_stream(document_file_path, datetime.datetime.now(), ".pdf", stream)
documents = [
    document,
]

# Indexing document from the stream
options = IndexingOptions()
index.add(documents, options)

# Closing the document stream after indexing is complete
stream.close()

print("Documents found:", index.search("Einstein").document_count)