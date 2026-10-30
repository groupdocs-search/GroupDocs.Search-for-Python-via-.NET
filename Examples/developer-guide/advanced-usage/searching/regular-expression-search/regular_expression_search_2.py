import os

from groupdocs.search import Index, RegexOptions, SearchQuery

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating a regular expression query with the specified options
regex_options = RegexOptions.IGNORE_CASE | RegexOptions.CULTURE_INVARIANT
query = SearchQuery.create_regex_query("^(.)\\1{1,}", regex_options)  # Search for two or more identical characters at the beginning of a word
result = index.search(query)

# Printing the words found in each document
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path), document.terms)