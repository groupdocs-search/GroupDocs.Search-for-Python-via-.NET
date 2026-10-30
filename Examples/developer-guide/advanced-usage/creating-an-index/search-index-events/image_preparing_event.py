from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# Creating an index
index = Index("./index")


# Subscribing to the event
def on_image_preparing(sender, args):
    print("Document:", args.document_key)
    print("Image inner path:", "/".join(args.inner_path))
    print("Image index:", args.image_index)
    print("Image frames:", len(args.image_frames))


index.events.image_preparing += on_image_preparing

# Indexing images of separate image files and images embedded in documents
options = IndexingOptions()
options.image_indexing_options.enabled_for_separate_images = True
options.image_indexing_options.enabled_for_embedded_images = True

# Indexing files
index.add("./documents", options)