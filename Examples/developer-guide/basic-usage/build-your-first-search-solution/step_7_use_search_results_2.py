import os

from groupdocs.search import Index
from groupdocs.search.common import FileOutputAdapter
from groupdocs.search.highlighters import DocumentHighlighter
from groupdocs.search.options import OutputFormat

index = Index("./index")
index.add("./documents")

query = "Einstein"  # Specify a search query

result = index.search(query)  # Search in the index
if result.document_count > 0:
    document = result.get_found_document(0)  # Getting the first found document
    os.makedirs("./output", exist_ok=True)
    output_adapter = FileOutputAdapter(OutputFormat.HTML, "./output/Highlighted.html")  # Creating the output adapter to a file
    highlighter = DocumentHighlighter(output_adapter)  # Creating the highlighter object
    index.highlight(document, highlighter)  # Generating output HTML formatted document with highlighted search results