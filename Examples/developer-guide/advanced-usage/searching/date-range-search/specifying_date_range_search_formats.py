import os

from groupdocs.search import Index
from groupdocs.search.options import DateFormat, DateFormatElement, SearchOptions

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Setting date formats
options = SearchOptions()
options.date_formats.clear()  # Removing default date formats
elements = [
    DateFormatElement.MONTH_TWO_DIGITS,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.DAY_OF_MONTH_TWO_DIGITS,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.YEAR_FOUR_DIGITS,
]
# Creating a date format pattern 'MM/dd/yyyy'
date_format = DateFormat(elements, "/")
options.date_formats.add(date_format)

# Searching in the index.
# For the given query, for example, the date 09/27/2019 will be found,
# but the date 2019-09-27 will not be found, because it is presented in a format that is not specified in the search options.
result = index.search("daterange(2017-01-01 ~~ 2019-12-31)", options)

# Printing the documents found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))