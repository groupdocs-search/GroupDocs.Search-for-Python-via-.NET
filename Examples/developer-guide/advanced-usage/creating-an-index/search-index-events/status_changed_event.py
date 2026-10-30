import threading

from groupdocs.search import Index
from groupdocs.search.common import IndexStatus
from groupdocs.search.options import IndexingOptions

# Creating an index
index = Index("./index")

completed = threading.Event()


# Subscribing to the event
def on_status_changed(sender, args):
    if args.status == IndexStatus.READY or args.status == IndexStatus.FAILED:
        # A notification of the operation completion
        print("The operation is completed. Index status:", args.status.name)
        completed.set()


index.events.status_changed += on_status_changed

# Setting the flag for asynchronous indexing
options = IndexingOptions()
options.is_async = True

# Asynchronous indexing documents from the specified folder
# The method terminates before the operation completes
index.add("./documents", options)

# Waiting for the notification
completed.wait()