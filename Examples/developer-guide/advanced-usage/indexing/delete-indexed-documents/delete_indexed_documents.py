import datetime
import io
import os

from groupdocs.search import Index
from groupdocs.search.common import Document, DocumentSourceKind
from groupdocs.search.options import IndexingOptions, UpdateOptions


# Implementing document loader
class DocumentLoader(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.document_key = os.path.basename(file_path)

    def close_document(self):
        pass

    def load_document(self):
        extension = os.path.splitext(self.file_path)[1]
        with open(self.file_path, "rb") as f:
            buffer = f.read()
        stream = io.BytesIO(buffer)
        document = Document.create_from_stream(self.document_key, datetime.datetime.now(), extension, stream)
        return document


file_path = "./sample.pdf"

# Creating an index in the specified folder
index = Index("./index")

# Indexing the document from stream
document_loader = DocumentLoader(file_path)
document = Document.create_lazy(DocumentSourceKind.STREAM, document_loader.document_key, document_loader)
documents = [document]
index.add(documents, IndexingOptions())

# Searching in the index
search_result = index.search("Einstein")
print("Documents found: " + str(search_result.document_count))

# Deleting indexed document from the index
document_keys = [document_loader.document_key]
delete_result = index.delete(UpdateOptions(), document_keys)
print("Deleted documents: " + str(delete_result.success_count))

# Physically removing the deleted documents from the index files
index.optimize()