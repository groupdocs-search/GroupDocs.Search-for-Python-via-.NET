import threading

from groupdocs.search import Index
from groupdocs.search.common import IndexStatus
from groupdocs.search.options import IndexingOptions

# Creating index in the specified folder
index = Index("./index")


# Subscribing to the event
def on_status_changed(sender, args):
    if args.status == IndexStatus.READY or args.status == IndexStatus.FAILED:
        # A notification of the operation completion should be here
        print("Index status:", args.status.name)


index.events.status_changed += on_status_changed

# The operation_finished event is raised when the operation is completed
finished = threading.Event()
index.events.operation_finished += lambda sender, args: finished.set()

# Creating an instance of indexing options
options = IndexingOptions()
options.is_async = True  # Specifying the asynchronous performing of the operation

# Indexing documents from the specified folder
# The method will return control before the indexing operation is completed
index.add("./documents", options)

# Waiting for the operation to complete before using the index
finished.wait()
print("Documents found:", index.search("Einstein").document_count)