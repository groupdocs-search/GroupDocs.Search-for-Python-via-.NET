from groupdocs.search import IndexSettings
from groupdocs.search.options import DocumentFilter

settings = IndexSettings()
document_filter = DocumentFilter.create_file_extension(".htm", ".html")
inverted_filter = DocumentFilter.create_not(document_filter)  # Inverting file extension filter to allow all extensions except of HTM and HTML
settings.document_filter = inverted_filter

print(settings.document_filter)