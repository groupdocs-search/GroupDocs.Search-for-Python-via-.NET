import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import CommonFieldNames

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search in the content field with text query
result1 = index.search("content: Einstein")

# Search in the content field with object query
word_query = SearchQuery.create_word_query("Einstein")
field_query = SearchQuery.create_field_query(CommonFieldNames.CONTENT, word_query)
result2 = index.search(field_query)

# Search in all fields, for comparison
result3 = index.search("Einstein")

# Printing the documents found and the fields in which the word was found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), [field.field_name for field in document.found_fields])
print("Documents found in all fields:", result3.document_count)
for document in result3:
    print("   ", os.path.basename(document.document_info.file_path), [field.field_name for field in document.found_fields])