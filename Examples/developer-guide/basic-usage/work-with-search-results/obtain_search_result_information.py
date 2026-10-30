from groupdocs.search import Index
from groupdocs.search.options import SearchOptions, TableDiscreteFunction

# Creating an index
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Creating search options
options = SearchOptions()
options.fuzzy_search.enabled = True  # Enabling the fuzzy search
options.fuzzy_search.fuzzy_algorithm = TableDiscreteFunction(3)  # Setting the maximum number of differences to 3

# Search for documents containing the word 'Einstein' or the phrase 'Theory of Relativity'
result = index.search('Einstein OR "Theory of Relativity"', options)

# Printing the result
print("Documents:", result.document_count)
print("Total occurrences:", result.occurrence_count)
for i in range(result.document_count):
    document = result.get_found_document(i)
    print("\tDocument:", document.document_info.file_path)
    print("\tOccurrences:", document.occurrence_count)
    for field in document.found_fields:
        print("\t\tField:", field.field_name)
        print("\t\tOccurrences:", field.occurrence_count)
        # Printing found terms
        if field.terms is not None:
            for term, occurrences in zip(field.terms, field.terms_occurrences):
                print("\t\t\t" + term.ljust(20) + str(occurrences))
        # Printing found phrases
        if field.term_sequences is not None:
            for sequence, occurrences in zip(field.term_sequences, field.term_sequences_occurrences):
                print("\t\t\t" + " ".join(sequence).ljust(30) + str(occurrences))