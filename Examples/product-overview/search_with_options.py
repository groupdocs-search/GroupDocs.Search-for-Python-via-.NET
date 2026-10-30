import os

from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

def search_with_options():
    with Index("./index") as index:
        index.add("./documents")

        # Fuzzy search also finds words that differ from the query by a few characters
        options = SearchOptions()
        options.fuzzy_search.enabled = True

        result = index.search("Einstien", options)
        print("Documents found:", result.document_count)
        for document in sorted(result, key=lambda found: found.relevance, reverse=True):
            print(os.path.basename(document.document_info.file_path), "-", document.occurrence_count, "occurrences")

if __name__ == "__main__":
    search_with_options()