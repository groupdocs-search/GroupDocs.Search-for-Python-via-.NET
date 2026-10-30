from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Searching in index
result1 = index.search("Einstein")
result2 = index.search('"Theory of Relativity"')

# Getting search reports
reports = index.get_search_reports()

# Printing reports to the console
for report in reports:
    print("Query: " + report.to_string())
    print("Time: " + str(report.start_time))
    print("Duration: " + str(report.search_duration))
    print("Documents: " + str(report.document_count))
    print("Occurrences: " + str(report.occurrence_count))
    print()