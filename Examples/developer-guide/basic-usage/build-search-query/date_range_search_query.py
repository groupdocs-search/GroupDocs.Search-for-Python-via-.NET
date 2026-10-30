from groupdocs.search import Index
from groupdocs.search.options import DateFormat, DateFormatElement, SearchOptions

index = Index("./index")
index.add("./documents")

options = SearchOptions()  # Creating a search options object
options.date_formats.clear()  # Removing default date formats

# Creating a date format pattern 'MM/dd/yyyy'
elements = [
    DateFormatElement.MONTH_TWO_DIGITS,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.DAY_OF_MONTH_TWO_DIGITS,
    DateFormatElement.DATE_SEPARATOR,
    DateFormatElement.YEAR_FOUR_DIGITS,
]
date_format = DateFormat(elements, "/")

options.date_formats.add(date_format)  # Adding the date format pattern to the date format collection
query = "daterange(2000-01-01 ~~ 2001-06-15)"  # Dates in the search query are always specified in the format 'yyyy-MM-dd'

result = index.search(query, options)  # Search in index
print("Documents found:", result.document_count)