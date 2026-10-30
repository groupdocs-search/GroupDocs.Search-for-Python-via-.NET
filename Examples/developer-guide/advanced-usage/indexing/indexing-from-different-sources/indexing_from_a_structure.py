import datetime

from groupdocs.search import Index
from groupdocs.search.common import Document, DocumentField
from groupdocs.search.options import CommonFieldNames, IndexingOptions

document_file_path = "./sample.txt"

# Creating an index
index = Index("./index")

# Creating a document object
with open(document_file_path, encoding="utf-8") as f:
    text = f.read()
fields = [
    DocumentField(CommonFieldNames.CONTENT, text),
]
document = Document.create_from_structure("ExampleDocument", datetime.datetime.now(), fields)
documents = [
    document,
]

# Indexing document from the structure
options = IndexingOptions()
index.add(documents, options)

print("Documents found:", index.search("Einstein").document_count)