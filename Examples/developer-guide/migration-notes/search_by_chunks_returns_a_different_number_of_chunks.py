from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

index = Index("./index")
index.add("./documents")
options = SearchOptions()
options.is_chunk_search = True

result = index.search("Einstein", options)
document_count = result.document_count
while result.next_chunk_search_token is not None:
    result = index.search_next(result.next_chunk_search_token)
    document_count += result.document_count
print("Documents found:", document_count)