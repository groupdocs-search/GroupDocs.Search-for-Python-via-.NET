import os

from groupdocs.search import Index
from groupdocs.search.common import FileOutputAdapter
from groupdocs.search.options import OutputFormat

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Getting list of indexed documents
documents = index.get_indexed_documents()

# Getting a document text
if len(documents) > 0:
    os.makedirs("./output", exist_ok=True)
    output_adapter = FileOutputAdapter(OutputFormat.HTML, "./output/Text.html")
    index.get_document_text(documents[0], output_adapter)
    print("The text of", os.path.basename(documents[0].file_path), "is saved to ./output/Text.html")