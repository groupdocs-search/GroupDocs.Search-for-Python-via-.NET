import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import FileOutputAdapter, StreamOutputAdapter, StringOutputAdapter, StructureOutputAdapter
from groupdocs.search.options import Compression, OutputFormat, TextStorageSettings

# Creating an index settings instance
settings = IndexSettings()
settings.text_storage_settings = TextStorageSettings(Compression.HIGH)  # Enabling storage of extracted text in the index

# Creating an index in the specified folder
index = Index("./index", settings)

# Indexing documents from the specified folder
index.add("./documents")

# Getting list of indexed documents
documents = index.get_indexed_documents()

# Getting a document text
if len(documents) > 0:
    document = documents[0]
    os.makedirs("./output", exist_ok=True)

    # Output to a file
    file_output_adapter = FileOutputAdapter(OutputFormat.HTML, "./output/Text.html")
    index.get_document_text(document, file_output_adapter)

    # Output to a stream
    with open("./output/Stream.html", "wb") as stream:
        stream_output_adapter = StreamOutputAdapter(OutputFormat.HTML, stream)
        index.get_document_text(document, stream_output_adapter)

    # Output to a string
    string_output_adapter = StringOutputAdapter(OutputFormat.HTML)
    index.get_document_text(document, string_output_adapter)
    html_text = string_output_adapter.get_result()
    print(html_text)

    # Output to a structure
    structure_output_adapter = StructureOutputAdapter(OutputFormat.PLAIN_TEXT)
    index.get_document_text(document, structure_output_adapter)
    fields = structure_output_adapter.get_result()
    print(document.to_string())
    for field in fields:
        print("\t" + field.name)