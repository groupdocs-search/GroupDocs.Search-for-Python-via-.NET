from groupdocs.search import Index

documents_folder1 = "./documents"
documents_folder2 = "./documents2"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents
index.add(documents_folder1)
index.add(documents_folder2)

# Getting indexing reports
reports = index.get_indexing_reports()

# Printing information from reports to the console
for report in reports:
    print("Time: " + str(report.start_time))
    print("Duration: " + str(report.indexing_time))
    print("Documents total: " + str(report.total_documents_in_index))
    print("Terms total: " + str(report.total_term_count))
    print("Indexed documents size (MB): " + str(report.indexed_documents_size))
    print("Index size (MB): " + str(report.total_index_size / 1024.0 / 1024.0))
    print("Segments: " + str(report.segment_count))
    print("Indexed documents: " + str(len(report.indexed_documents)))
    for error in report.errors:
        print("Error: " + error)
    print()