import os

from groupdocs.search import Index

def searching_limitations():
    with Index("./index") as index:
        index.add("./documents")

        result = index.search("contract")
        # Only the first 10 found documents are available in the evaluation mode
        count = min(result.document_count, 10)
        for i in range(count):
            document = result.get_found_document(i)
            print(os.path.basename(document.document_info.file_path))

if __name__ == "__main__":
    searching_limitations()