import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.common import WordPattern

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search for the phrase in text form
query1 = '"Test?(0~1) *1~~2 relativity"'
result1 = index.search(query1)

# Search for the phrase in object form
pattern = WordPattern()
pattern.append_string("Test")
pattern.append_wildcard(0, 1)
word_pattern1 = SearchQuery.create_word_pattern_query(pattern)
wildcard2 = SearchQuery.create_wildcard_query(1, 2)
word3 = SearchQuery.create_word_query("relativity")
query2 = SearchQuery.create_phrase_search_query(word_pattern1, wildcard2, word3)
result2 = index.search(query2)

# The search can find the following phrases:
# "Test of special relativity"
# "Tests of special relativity"
# "Test of general relativity"
# "Tests of general relativity"

# Printing the phrases found
# (stop words and the words matched by a wildcard are reported as *)
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path))
    for field in document.found_fields:
        for sequence in field.term_sequences:
            print("       ", " ".join(sequence))