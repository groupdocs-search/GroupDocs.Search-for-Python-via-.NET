import os

from groupdocs.search import Index
from groupdocs.search.common import SearchImage
from groupdocs.search.options import ImageSearchOptions, IndexingOptions, SearchDocumentFilter

# Creating an index
index = Index("./index")

# Setting the image indexing options
indexing_options = IndexingOptions()
indexing_options.image_indexing_options.enabled_for_container_item_images = True
indexing_options.image_indexing_options.enabled_for_embedded_images = True
indexing_options.image_indexing_options.enabled_for_separate_images = True

# Indexing documents in a document folder
index.add("./documents", indexing_options)

# Setting the image search options
image_search_options = ImageSearchOptions()
image_search_options.hash_differences = 10
image_search_options.max_result_count = 100
image_search_options.search_document_filter = SearchDocumentFilter.create_file_extension(".zip", ".png", ".jpg")

# Creating a reference image for search
search_image = SearchImage.create("./image.png")

# Searching in the index
result = index.search(search_image, image_search_options)

print("Images found: " + str(result.image_count))
for i in range(result.image_count):
    image = result.get_found_image(i)
    document_info = image.document_info
    name = os.path.basename(document_info.file_path)
    if document_info.inner_path:
        name += " / " + document_info.inner_path  # An item of a container document, such as a ZIP archive
    print(name + ", image " + str(image.image_index) + ", frame " + str(image.frame_index) + ", different bits: " + str(image.hash_differences))