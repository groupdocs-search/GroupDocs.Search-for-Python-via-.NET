from groupdocs.search import Index
from groupdocs.search.common import Document
from groupdocs.search.options import IndexingOptions

document_file_path = "./sample.pdf"

# Creating an index
index = Index("./index")

# Creating a document object
document = Document.create_from_file(document_file_path)
documents = [
    document,
]

# Indexing document from the file
options = IndexingOptions()
index.add(documents, options)

print("Documents found:", index.search("Einstein").document_count)