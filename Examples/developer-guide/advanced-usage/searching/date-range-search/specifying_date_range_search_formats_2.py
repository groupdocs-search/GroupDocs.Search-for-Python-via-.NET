import os

from groupdocs.search import Index
from groupdocs.search.options import DateFormat, DateFormatElement, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a date format pattern 'dd.MMMM.yyyy' with the date separator and month names of the German culture
elements = [
    DateFormatElement.DAY_OF_MONTH_TWO_DIGITS,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.MONTH_FULL_NAME,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.YEAR_FOUR_DIGITS,
]
date_format = DateFormat("de-DE", elements)

# Adding the format to the default date formats
options = SearchOptions()
options.date_formats.add(date_format)
print("Date formats:", ", ".join(f.to_string() for f in options.date_formats))

# Searching in the index
result = index.search("daterange(2017-01-01 ~~ 2019-12-31)", options)

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))