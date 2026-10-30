import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import CommonFieldNames

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a query that searches for the phrase 'theory of * relativity' in the content field
phrase_query = SearchQuery.create_phrase_search_query(
    SearchQuery.create_word_query("theory"),
    SearchQuery.create_word_query("of"),
    SearchQuery.create_wildcard_query(0, 1),
    SearchQuery.create_word_query("relativity"))
field_query = SearchQuery.create_field_query(CommonFieldNames.CONTENT, phrase_query)

# Printing the query tree
print(field_query.to_string())
for i in range(phrase_query.child_count):
    child = phrase_query.get_child(i)
    print("\t" + child.to_string() + " (field: " + str(child.field_name) + ")")

# Searching in the index
result = index.search(field_query)

# Printing the documents and the phrases found
# (stop words and the words matched by a wildcard are reported as *)
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))
    for field in document.found_fields:
        for sequence in field.term_sequences:
            print("       ", " ".join(sequence))