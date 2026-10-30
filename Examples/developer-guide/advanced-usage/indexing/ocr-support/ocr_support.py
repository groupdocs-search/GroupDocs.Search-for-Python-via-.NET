from groupdocs.search import Index
from groupdocs.search.options import ImageLocation, IndexingOptions

try:
    import easyocr  # pip install easyocr
except ImportError:
    easyocr = None


# Implementing the OCR connector that uses the EasyOCR package
class EasyOcrConnector(object):
    def __init__(self):
        self.reader = easyocr.Reader(["en"]) if easyocr is not None else None

    def recognize(self, context):
        extension = context.image_file_extension.lower()
        if context.image_location == ImageLocation.SEPARATE:
            if extension in (".gif", ".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ""):
                return self.recognize_private(context)
            return None
        elif context.image_location in (ImageLocation.EMBEDDED, ImageLocation.CONTAINER_ITEM):
            return self.recognize_private(context)
        else:
            raise NotImplementedError("The image type is not supported: " + str(context.image_location))

    def recognize_private(self, context):
        image = context.image_stream.read()  # Reading the whole image stream
        if self.reader is None:
            # Without EasyOCR, the connector only reports the image it receives
            print("Image: %s, extension '%s', %d bytes"
                  % (context.image_location.name, context.image_file_extension, len(image)))
            return None
        return " ".join(self.reader.readtext(image, detail=0))


# Creating an index
index = Index("./index")

# Setting the OCR indexing options
options = IndexingOptions()
options.ocr_indexing_options.enabled_for_separate_images = True
options.ocr_indexing_options.enabled_for_embedded_images = True
options.ocr_indexing_options.ocr_connector = EasyOcrConnector()

# Indexing documents in a document folder
index.add("./documents", options)

# Searching in the index
result = index.search("Einstein")
print("Documents found:", result.document_count)