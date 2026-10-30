import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import CommonFieldNames

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with text query
result1 = index.search("(filename: (Albert AND Einstein)) OR (content: (\"theory of relativity\" OR \"special relativity\"))")

# Search with object query
albert_query = SearchQuery.create_word_query("Albert")
einstein_query = SearchQuery.create_word_query("Einstein")
and_query = SearchQuery.create_and_query(albert_query, einstein_query)
filename_query = SearchQuery.create_field_query(CommonFieldNames.FILE_NAME, and_query)

theory_query = SearchQuery.create_word_query("theory")
of_query = SearchQuery.create_word_query("of")
relativity1_query = SearchQuery.create_word_query("relativity")
special_query = SearchQuery.create_word_query("special")
relativity2_query = SearchQuery.create_word_query("relativity")

phrase1_query = SearchQuery.create_phrase_search_query(theory_query, of_query, relativity1_query)
phrase2_query = SearchQuery.create_phrase_search_query(special_query, relativity2_query)
or_query = SearchQuery.create_or_query(phrase1_query, phrase2_query)
content_query = SearchQuery.create_field_query(CommonFieldNames.CONTENT, or_query)

root_query = SearchQuery.create_or_query(filename_query, content_query)
result2 = index.search(root_query)

# Printing the documents found and the fields in which they were found
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path), [field.field_name for field in document.found_fields])