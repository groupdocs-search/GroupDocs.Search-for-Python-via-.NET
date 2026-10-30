import os

from groupdocs.search import Index

def quick_example():
    # Create an index in the "index" folder, or open the one already there
    with Index("./index") as index:
        # Index every supported document in the "documents" folder
        index.add("./documents")

        # Search the index and list the documents found
        result = index.search("relativity")
        print("Documents found:", result.document_count)
        # Most relevant first: the result lists the documents in the order they were indexed
        for document in sorted(result, key=lambda found: found.relevance, reverse=True):
            print(os.path.basename(document.document_info.file_path), "-", document.occurrence_count, "occurrences")

if __name__ == "__main__":
    quick_example()