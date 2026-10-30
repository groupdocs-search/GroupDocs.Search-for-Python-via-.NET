import datetime
import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search for dates using query in text form
query1 = "daterange(2017-01-01 ~~ 2019-12-31)"
result1 = index.search(query1)

# Search for dates using query in object form
query2 = SearchQuery.create_date_range_query(datetime.datetime(2017, 1, 1), datetime.datetime(2019, 12, 31))
result2 = index.search(query2)

# Printing the documents found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path))