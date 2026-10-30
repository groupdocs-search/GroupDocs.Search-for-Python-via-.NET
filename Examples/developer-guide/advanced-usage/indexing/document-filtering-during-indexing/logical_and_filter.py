import datetime

from groupdocs.search import IndexSettings
from groupdocs.search.options import DocumentFilter

settings = IndexSettings()
filter1 = DocumentFilter.create_creation_time_range(datetime.datetime(2015, 1, 1), datetime.datetime(2016, 1, 1))
filter2 = DocumentFilter.create_file_extension(".txt")
filter3 = DocumentFilter.create_file_length_upper_bound(8 * 1024 * 1024)
final_filter = DocumentFilter.create_and(filter1, filter2, filter3)
settings.document_filter = final_filter

print(settings.document_filter)