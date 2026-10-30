from groupdocs.search import Index
from groupdocs.search.common import Cancellation
from groupdocs.search.options import MergeOptions

# Creating an index in the specified folder
index = Index("./index")

index.add("./documents")  # Indexing documents from the specified folder
index.add("./documents2")  # Each call to add creates at least one new segment in the index
index.add("./documents3")

options = MergeOptions()
options.cancellation = Cancellation()  # Creating cancellation object to be able to cancel the operation
options.cancellation.cancel_after(100000)  # Setting maximum duration of the operation to 100 seconds

# Merging segments of the index
index.optimize(options)

print("Segment count: " + str(index.index_info.segment_count))