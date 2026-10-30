import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import WordsFieldNames

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search in the company field with text query
query1 = WordsFieldNames.COMPANY + ": Dycum"
result1 = index.search(query1)

# Search in the company field with object query
word_query = SearchQuery.create_word_query("Dycum")
field_query = SearchQuery.create_field_query(WordsFieldNames.COMPANY, word_query)
result2 = index.search(field_query)

# Printing the documents found and the fields in which the word was found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), [field.field_name for field in document.found_fields])