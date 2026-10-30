from groupdocs.search import Index
from groupdocs.search.options import MergeOptions

index = Index("./index")
index.add("./documents")

other_index = Index("./other-index", True)
other_index.dictionaries.stop_word_dictionary.add_range(["physics"])
other_index.add("./documents")

try:
    index.merge(other_index, MergeOptions())
except RuntimeError as exception:
    # The indexes divide text into terms differently; the message names the differences
    print(exception)