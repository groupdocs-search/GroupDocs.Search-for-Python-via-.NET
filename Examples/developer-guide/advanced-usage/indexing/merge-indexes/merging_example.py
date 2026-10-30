from groupdocs.search import Index
from groupdocs.search.common import Cancellation
from groupdocs.search.options import MergeOptions

index1 = Index("./index1")  # Creating index1
index1.add("./documents")  # Indexing documents

index2 = Index("./index2")  # Creating index2
index2.add("./documents2")  # Indexing documents

options = MergeOptions()
options.cancellation = Cancellation()  # Creating cancellation object to be able to cancel the operation

try:
    # Merging index2 into index1
    # Files of index2 will not be changed
    index1.merge(index2, options)
except RuntimeError as exception:
    # The indexes divide text into terms differently; the message names the differences
    print(exception.message)

print("Documents in index1:", len(index1.get_indexed_documents()))