import os

from groupdocs.search import Index
from groupdocs.search.common import Notification

# Creating an index
index = Index("./index")

# Indexing documents in a document folder
index.add("./documents")

# Renaming a document
old_document_path = "./documents/OldDocumentName.txt"
new_document_path = "./documents/NewDocumentName.txt"
os.rename(old_document_path, new_document_path)

# Notifying the index about renaming
notification = Notification.create_rename_notification(old_document_path, new_document_path)
result = index.notify(notification)
print("Notification applied:", result)

# Updating the index
# The renamed document will not be reindexed
index.update()

for document in index.get_indexed_documents():
    print("Indexed:", os.path.basename(document.file_path))

# Restoring the original file name, so that the example can run again
os.rename(new_document_path, old_document_path)