import os

from groupdocs.search import Index
from groupdocs.search.common import DocumentField

# Defining somewhere a dictionary containing subjects of documents
subjects = {}
subjects[os.path.abspath("./documents/Bhagavad-Gita-lecture.pdf").lower()] = "Spiritual"
# ...

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_file_indexing(sender, args):
    subject = subjects.get(args.document_full_path.lower())  # Getting a subject for the current document
    if subject is not None:
        args.additional_fields = [  # Setting additional fields for the current document
            DocumentField("Subject", subject)
        ]


index.events.file_indexing += on_file_indexing

# Indexing documents from the specified folder
index.add("./documents")

# Searching in the added field
result = index.search("Subject:Spiritual")
for found in result:
    print("Found:", os.path.basename(found.document_info.file_path))