import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.options import DocumentFilter

# Creating a filter that skips documents with extensions '.doc', '.docx', '.rtf'
settings = IndexSettings()
file_extension_filter = DocumentFilter.create_file_extension(".doc", ".docx", ".rtf")  # Creating file extension filter that allows only specified extensions
inverted_filter = DocumentFilter.create_not(file_extension_filter)  # Inverting file extension filter to allow all extensions except specified ones
settings.document_filter = inverted_filter

# Creating an index in the specified folder
index = Index("./index", settings)

# Indexing documents
index.add("./documents")

for document in index.get_indexed_documents():
    print("Indexed:", os.path.basename(document.file_path))