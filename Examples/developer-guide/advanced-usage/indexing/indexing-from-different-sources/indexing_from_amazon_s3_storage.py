import datetime
import io

try:
    import boto3  # pip install boto3
except ImportError:
    boto3 = None

from groupdocs.search import Index
from groupdocs.search.common import Document, DocumentSourceKind
from groupdocs.search.options import IndexingOptions


class DocumentLoaderFromAmazon(object):
    def __init__(self, document_key, extension, storage_key):
        self.document_key = document_key
        self.extension = extension
        self.storage_key = storage_key

    def load_document(self):
        client = boto3.client("s3")
        bucket_name = "my-bucket"
        response = client.get_object(Bucket=bucket_name, Key=self.storage_key)
        memory_stream = io.BytesIO(response["Body"].read())
        document = Document.create_from_stream(self.document_key, datetime.datetime.now(), self.extension, memory_stream)
        return document

    def close_document(self):
        pass


key = "example.pdf"

# Creating an index
index = Index("./index")
# Reporting errors, for example, a document that cannot be loaded
index.events.error_occurred += lambda sender, args: print(args.message)

# Creating a document object
document_loader = DocumentLoaderFromAmazon("documentKey", ".pdf", key)
document = Document.create_lazy(DocumentSourceKind.STREAM, "documentKey", document_loader)
documents = [
    document,
]

# Indexing the lazy-loaded document
if boto3 is None:
    print("boto3 is not installed (pip install boto3), so the document is not indexed")
else:
    options = IndexingOptions()
    index.add(documents, options)

print("Indexed documents:", len(index.get_indexed_documents()))