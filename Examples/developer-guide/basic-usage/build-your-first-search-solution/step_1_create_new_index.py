from groupdocs.search import Index

# Creating an index in the specified folder
index = Index("./index")
print("Index folder:", index.index_info.index_folder)