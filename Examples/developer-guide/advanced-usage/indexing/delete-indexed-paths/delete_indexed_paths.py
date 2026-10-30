from groupdocs.search import Index
from groupdocs.search.options import UpdateOptions

documents_folder1 = "./documents"
documents_folder2 = "./documents2"

# Creating an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folders
index.add(documents_folder1)
index.add(documents_folder2)

# Getting indexed paths from the index
indexed_paths1 = index.get_indexed_paths()

# Writing indexed paths to the console
print("Indexed paths:")
for path in indexed_paths1:
    print("\t" + path)

# Deleting indexed path from the index
delete_result = index.delete([documents_folder1], UpdateOptions())

# Getting indexed paths after deletion
indexed_paths2 = index.get_indexed_paths()
print("\nDeleted paths: " + str(delete_result.success_count))

print("\nIndexed paths:")
for path in indexed_paths2:
    print("\t" + path)