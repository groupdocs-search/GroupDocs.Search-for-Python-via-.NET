import datetime
import io

try:
    from azure.storage.blob import BlobClient  # pip install azure-storage-blob
except ImportError:
    BlobClient = None

from groupdocs.search import Index
from groupdocs.search.common import Document, DocumentSourceKind
from groupdocs.search.options import IndexingOptions


class DocumentLoaderFromAzure(object):
    def __init__(self, document_key, extension, blob_name):
        self.document_key = document_key
        self.extension = extension
        self.blob_name = blob_name

    def load_document(self):
        connection_string = "***"  # The connection string of the storage account
        container_name = "***"
        blob_client = BlobClient.from_connection_string(connection_string, container_name, self.blob_name)

        memory_stream = io.BytesIO(blob_client.download_blob().readall())

        document = Document.create_from_stream(self.document_key, datetime.datetime.now(), self.extension, memory_stream)
        return document

    def close_document(self):
        pass


blob_name = "example.pdf"

# Creating an index
index = Index("./index")
# Reporting errors, for example, a document that cannot be loaded
index.events.error_occurred += lambda sender, args: print(args.message)

# Creating a document object
document_loader = DocumentLoaderFromAzure("documentKey", ".pdf", blob_name)
document = Document.create_lazy(DocumentSourceKind.STREAM, "documentKey", document_loader)
documents = [
    document,
]

# Indexing the lazy-loaded document
if BlobClient is None:
    print("azure-storage-blob is not installed (pip install azure-storage-blob), so the document is not indexed")
else:
    options = IndexingOptions()
    index.add(documents, options)

print("Indexed documents:", len(index.get_indexed_documents()))