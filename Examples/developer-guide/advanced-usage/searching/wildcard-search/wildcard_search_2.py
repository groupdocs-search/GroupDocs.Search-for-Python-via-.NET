import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.common import WordPattern

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Search with pattern "m?rry"
# Search for 'merry', 'marry', etc.
pattern1 = WordPattern()
pattern1.append_string("m")
pattern1.append_one_character_wildcard()
pattern1.append_string("rry")
query1 = SearchQuery.create_word_pattern_query(pattern1)
result1 = index.search(query1)

# Search with pattern "card?(1~6)"
# Search for 'cardiff', 'cardinal', 'cardio', 'cards', etc.
pattern2 = WordPattern()
pattern2.append_string("card")
pattern2.append_wildcard(1, 6)
query2 = SearchQuery.create_word_pattern_query(pattern2)
result2 = index.search(query2)

# Printing the words found
for pattern, result in ((pattern1, result1), (pattern2, result2)):
    print(pattern.to_string(), "- documents found:", result.document_count)
    for document in result:
        print("   ", os.path.basename(document.document_info.file_path), document.terms)