from groupdocs.search import Index, IndexRepository

# Creating an index repository instance
index_repository = IndexRepository()

# Creating or loading an index and adding to the index repository
index1 = Index("./index1")
index_repository.add_to_repository(index1)

# Creating an index via the index repository by calling a single method
index2 = index_repository.create("./index2")

# Adding documents to the index 1
index1.add("./documents1")

# Adding documents to the index 2
index2.add("./documents2")

print("Indexes in the repository:", len(index_repository.indexes))