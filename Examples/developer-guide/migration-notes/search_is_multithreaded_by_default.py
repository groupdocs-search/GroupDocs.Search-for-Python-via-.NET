from groupdocs.search import Index
from groupdocs.search.options import NumberOfThreads

index = Index("./index")
index.add("./documents")
index.index_settings.search_threads = NumberOfThreads.ONE  # The value is saved in the index

result = index.search("^relativ.*")
print("Documents found:", result.document_count)