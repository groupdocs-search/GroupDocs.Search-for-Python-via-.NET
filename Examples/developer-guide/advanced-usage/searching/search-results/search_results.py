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
print("Documents: " + str(result.document_count))
print("Total occurrences: " + str(result.occurrence_count))
for i in range(result.document_count):
    document = result.get_found_document(i)
    print("\tDocument: " + document.document_info.file_path)
    print("\tOccurrences: " + str(document.occurrence_count))
    for field in document.found_fields:
        print("\t\tField: " + field.field_name)
        print("\t\tOccurrences: " + str(field.occurrence_count))
        # Printing found terms
        if field.terms is not None:
            for k in range(len(field.terms)):
                print("\t\t\t" + field.terms[k].ljust(20) + str(field.terms_occurrences[k]))
        # Printing found phrases
        if field.term_sequences is not None:
            for k in range(len(field.term_sequences)):
                sequence = " ".join(field.term_sequences[k])
                print("\t\t\t" + sequence.ljust(30) + str(field.term_sequences_occurrences[k]))