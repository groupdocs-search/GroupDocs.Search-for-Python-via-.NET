import os

from groupdocs.search import Index
from groupdocs.search.common import FileOutputAdapter
from groupdocs.search.highlighters import DocumentHighlighter
from groupdocs.search.options import OutputFormat

# Creating an index
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search for the word 'eternity'
result = index.search("eternity")

# Highlighting occurrences in text
if result.document_count > 0:
    document = result.get_found_document(0)  # Getting the first found document
    os.makedirs("./output", exist_ok=True)
    output_adapter = FileOutputAdapter(OutputFormat.HTML, "./output/Highlighted.html")  # Creating an output adapter to the file
    highlighter = DocumentHighlighter(output_adapter)  # Creating the highlighter object
    index.highlight(document, highlighter)  # Generating HTML formatted text with highlighted occurrences