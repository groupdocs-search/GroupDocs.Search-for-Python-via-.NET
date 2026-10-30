from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# Creating an index
index = Index("./index")

# Setting the metadata indexing options
options = IndexingOptions()
options.metadata_indexing_options.default_field_name = "default"
options.metadata_indexing_options.separator_in_compound_name = "\\"
options.metadata_indexing_options.max_bytes_to_index_field = 10
options.metadata_indexing_options.max_ints_to_index_field = 10
options.metadata_indexing_options.max_longs_to_index_field = 10
options.metadata_indexing_options.max_doubles_to_index_field = 10

# Starting indexing operation
index.add("./documents", options)

print("Indexed documents:", len(index.get_indexed_documents()))