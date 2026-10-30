import os

from groupdocs.search import Index, License
from groupdocs.search.options import SearchOptions

def fuzzy_search():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Search.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    with Index("./index") as index:
        index.add("./documents")

        # Fuzzy search also finds words that differ from the query by a few characters
        options = SearchOptions()
        options.fuzzy_search.enabled = True

        result = index.search("Einstien", options)
        print("Documents found:", result.document_count)
        for document in sorted(result, key=lambda found: found.relevance, reverse=True):
            # The words of the document that matched the query
            words = set()
            for field in document.found_fields:
                words.update(field.terms)
            print(os.path.basename(document.document_info.file_path), "-", ", ".join(sorted(words)))

if __name__ == "__main__":
    fuzzy_search()