from groupdocs.search import Index

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_operation_progress_changed(sender, args):
    print("Last processed:", args.last_document_path)
    print("Result:", args.last_document_status.name)
    print("Processed documents:", args.processed_documents)
    print("Skipped documents:", args.skipped_documents)
    print("Total documents:", args.total_documents)
    print("Progress percentage:", args.progress_percentage)


index.events.operation_progress_changed += on_operation_progress_changed

# Indexing documents from the specified folder
index.add("./documents")