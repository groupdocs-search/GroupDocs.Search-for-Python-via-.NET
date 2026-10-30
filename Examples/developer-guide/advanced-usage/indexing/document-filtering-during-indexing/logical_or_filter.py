from groupdocs.search import IndexSettings
from groupdocs.search.options import DocumentFilter

settings = IndexSettings()
txt_filter = DocumentFilter.create_file_extension(".txt")
not_txt_filter = DocumentFilter.create_not(txt_filter)
bound5_filter = DocumentFilter.create_file_length_upper_bound(5 * 1024 * 1024)
bound10_filter = DocumentFilter.create_file_length_upper_bound(10 * 1024 * 1024)
txt_size_filter = DocumentFilter.create_and(txt_filter, bound5_filter)
not_txt_size_filter = DocumentFilter.create_and(not_txt_filter, bound10_filter)
final_filter = DocumentFilter.create_or(txt_size_filter, not_txt_size_filter)
settings.document_filter = final_filter

print(settings.document_filter)