from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions


# Implementing the OCR connector as a function
def recognize(context):
    image = context.image_stream.read()
    # Send the image to an OCR service here, for example, Aspose.OCR Cloud,
    # and return the text it recognizes
    print("Image to recognize: %s, extension '%s', %d bytes"
          % (context.image_location.name, context.image_file_extension, len(image)))
    return None


# Creating an index
index = Index("./index")

# Setting the OCR indexing options
options = IndexingOptions()
options.ocr_indexing_options.enabled_for_separate_images = True
options.ocr_indexing_options.ocr_connector = recognize

# Indexing documents in a document folder
index.add("./documents", options)