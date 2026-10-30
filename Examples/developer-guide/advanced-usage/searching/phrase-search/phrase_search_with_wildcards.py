import os

from groupdocs.search import Index, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search for the phrase with a wildcard in text form
query1 = '"theory *1~~2 relativity"'
result1 = index.search(query1)

# Search for the phrase with a wildcard in object form
word1 = SearchQuery.create_word_query("theory")
wildcard2 = SearchQuery.create_wildcard_query(1, 2)
word3 = SearchQuery.create_word_query("relativity")
query2 = SearchQuery.create_phrase_search_query(word1, wildcard2, word3)
result2 = index.search(query2)

# The search can find the following phrases:
# "theory of relativity"
# "theory of special relativity"

# Printing the phrases found
# (stop words and the words matched by a wildcard are reported as *)
print("Documents found by the text query:", result1.document_count)
print("Documents found by the object query:", result2.document_count)
for document in result2:
    print("   ", os.path.basename(document.document_info.file_path))
    for field in document.found_fields:
        for sequence in field.term_sequences:
            print("       ", " ".join(sequence))