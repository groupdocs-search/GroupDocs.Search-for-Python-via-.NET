import threading

from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# Creating an index
index = Index("./index")

finished = threading.Event()

# Subscribing to the event
def on_operation_finished(sender, args):
    # There should be a code indicating the completion of the operation
    print("Operation finished:", args.operation_type.name)
    finished.set()

index.events.operation_finished += on_operation_finished

# Setting the flag for asynchronous indexing
options = IndexingOptions()
options.is_async = True

# Asynchronous indexing documents from the specified folder
# The current method terminates before the operation completes
index.add("./documents", options)

# Other tasks can be performed here; then wait for the operation to complete
finished.wait()
print("Indexed documents:", len(index.get_indexed_documents()))