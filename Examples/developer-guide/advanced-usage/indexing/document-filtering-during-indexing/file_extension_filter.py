from groupdocs.search.options import DocumentFilter

# This filter allows indexing only FB2, EPUB, and TXT files
document_filter = DocumentFilter.create_file_extension(".fb2", ".epub", ".txt")

print(document_filter)