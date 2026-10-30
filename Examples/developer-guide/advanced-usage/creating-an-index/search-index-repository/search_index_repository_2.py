from groupdocs.search import Index, IndexRepository

# Creating an index repository instance
index_repository = IndexRepository()


# Subscribing to an event
def on_error_occurred(sender, args):
    print("Index:", args.index_folder)
    print("Error:", args.message)


index_repository.events.error_occurred += on_error_occurred

# Creating or loading an index and adding to the index repository
index1 = Index("./index1")
index_repository.add_to_repository(index1)

# Creating or loading an index and adding to the index repository
index2 = Index("./index2")
index_repository.add_to_repository(index2)

# Adding documents to the index 1
index1.add("./documents1")

# Adding documents to the index 2
index2.add("./documents2")

# Changing, deleting, adding documents to document folders
# ...

# Updating all indexes in the repository
index_repository.update()

# Searching in the repository
result = index_repository.search("Einstein")
print("Documents found:", result.document_count)