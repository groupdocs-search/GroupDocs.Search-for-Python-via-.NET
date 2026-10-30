from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

query = "Einstein"

# Creating an index in the specified folder
index = Index("./index")

# Subscribing to the event of errors
index.events.error_occurred += lambda sender, args: print(args.message)

# Indexing documents from the specified folder
index.add("./documents")

# Creating a search options instance with incompatible options
options = SearchOptions()
options.use_case_sensitive_search = True
options.fuzzy_search.enabled = True

# The search returns an empty result, and the error_occurred event reports the reason
result = index.search(query, options)
print("Document count: " + str(result.document_count))