import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import StructureOutputAdapter
from groupdocs.search.highlighters import DocumentHighlighter
from groupdocs.search.options import Compression, HighlightOptions, OutputFormat, TextStorageSettings

# Creating an index settings instance
settings = IndexSettings()
settings.text_storage_settings = TextStorageSettings(Compression.HIGH)  # Enabling storage of extracted text in the index

# Creating an index in the specified folder
index = Index("./index", settings)

# Indexing documents from the specified folder
index.add("./documents")

# Search for the word 'Universe'
result = index.search("Universe")

# Highlighting occurrences in the text
if result.document_count > 0:
    document = result.get_found_document(0)  # Getting the first found document
    output_adapter = StructureOutputAdapter(OutputFormat.PLAIN_TEXT)  # Creating the output adapter
    highlighter = DocumentHighlighter(output_adapter)  # Creating the highlighter instance
    options = HighlightOptions()  # Creating the highlight options
    options.term_highlight_start_tag = "<Term>"  # Setting the start tag for the found word
    options.term_highlight_end_tag = "</Term>"  # Setting the end tag for the found word
    index.highlight(document, highlighter, options)  # Generating plain text with highlighted occurrences

    fields = output_adapter.get_result()
    print(document.to_string())
    for field in fields:
        # Printing field names of the found document
        print("\t" + field.name)

    # Saving the plain text of the fields with highlighted occurrences to a file
    os.makedirs("./output", exist_ok=True)
    with open("./output/Highlighted.txt", "w", encoding="utf-8") as file:
        for field in fields:
            file.write(field.name + ": " + field.value + "\n")