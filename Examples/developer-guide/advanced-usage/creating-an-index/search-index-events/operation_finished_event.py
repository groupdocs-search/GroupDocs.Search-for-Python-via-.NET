import threading

from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# Creating an index
index = Index("./index")

finished = threading.Event()


# Subscribing to the event
def on_operation_finished(sender, args):
    # Writing operation details to the console
    print("Operation finished:", args.operation_type.name)
    print("Message:", args.message)
    print("Index folder:", args.index_folder)
    print("Time:", args.time)
    finished.set()


index.events.operation_finished += on_operation_finished

# Indexing documents from the specified folder
options = IndexingOptions()
options.is_async = True  # Enabling asynchronous indexing mode
index.add("./documents", options)

# The method returns before the operation completes, so waiting for the event
finished.wait()