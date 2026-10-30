import datetime
import io
import urllib.request

from groupdocs.search import Index
from groupdocs.search.common import Document, DocumentSourceKind
from groupdocs.search.options import IndexingOptions


class DocumentLoaderFromFtp(object):
    def __init__(self, document_key, url, extension):
        self.document_key = document_key
        self.url = url
        self.extension = extension

    def load_document(self):
        # urllib reads ftp:// URLs as well; credentials can be given as ftp://user:password@host/path
        with urllib.request.urlopen(self.url) as response:
            memory_stream = io.BytesIO(response.read())
        document = Document.create_from_stream(self.document_key, datetime.datetime.now(), self.extension, memory_stream)
        return document

    def close_document(self):
        pass


url = "ftp://example.com/ExampleDocument.pdf"

# Creating an index
index = Index("./index")
# Reporting errors, for example, a document that cannot be loaded
index.events.error_occurred += lambda sender, args: print(args.message)

# Creating a document object
document_key = url
document_loader = DocumentLoaderFromFtp(document_key, url, ".pdf")
document = Document.create_lazy(DocumentSourceKind.STREAM, document_key, document_loader)
documents = [
    document,
]

# Indexing the lazy-loaded document
options = IndexingOptions()
index.add(documents, options)

print("Indexed documents:", len(index.get_indexed_documents()))