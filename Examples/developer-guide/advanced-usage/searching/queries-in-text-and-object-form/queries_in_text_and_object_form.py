import os

from groupdocs.search import Index, SearchQuery
from groupdocs.search.options import SearchOptions, TableDiscreteFunction

# Creating index
index = Index("./index")

# Indexing
index.add("./documents")

# Creating subquery 1 - simple word query
subquery1 = SearchQuery.create_word_query("future")
subquery1.search_options = SearchOptions()  # Setting search options only for subquery 1
subquery1.search_options.fuzzy_search.enabled = True
subquery1.search_options.fuzzy_search.fuzzy_algorithm = TableDiscreteFunction(3)  # The maximum number of differences is 3

# Creating subquery 2 - numeric range query
subquery2 = SearchQuery.create_numeric_range_query(1, 1000000)

# Creating subquery 3 - regular expression query
subquery3 = SearchQuery.create_regex_query(r"(.)\1")

# Combining subqueries into one query - phrase search query
query = SearchQuery.create_phrase_search_query(subquery1, subquery2, subquery3)

# Creating overall search options that limit the number of occurrences returned
options = SearchOptions()
options.max_occurrence_count_per_term = 1000000
options.max_total_occurrence_count = 10000000

# Searching
result = index.search(query, options)

# The result may contain the following word sequences:
# future 12 balloons
# picture 3 balloons

# Printing the word sequences found
print("Documents found:", result.document_count)
for document in result:
    print("   ", os.path.basename(document.document_info.file_path))
    for field in document.found_fields:
        for sequence in field.term_sequences:
            print("       ", " ".join(sequence))