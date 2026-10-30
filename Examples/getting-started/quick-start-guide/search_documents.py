import os

from groupdocs.search import Index, License

def search_documents():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Search.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    # Create an index in the "index" folder and index the "documents" folder
    with Index("./index") as index:
        index.add("./documents")

        # A phrase in double quotes matches these words in this order
        result = index.search('"theory of relativity"')

        print("Documents found:", result.document_count)
        print("Occurrences found:", result.occurrence_count)
        # Most relevant first: the result lists the documents in the order they were indexed
        for document in sorted(result, key=lambda found: found.relevance, reverse=True):
            print(os.path.basename(document.document_info.file_path), "-", document.occurrence_count, "occurrences")

if __name__ == "__main__":
    search_documents()