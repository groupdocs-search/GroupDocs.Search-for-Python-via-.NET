import io

from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

try:
    # pip install pytesseract pillow
    # The Tesseract OCR engine with the English language data must be installed too
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None


# Implementing the OCR connector that uses Tesseract
class TesseractOcrConnector(object):
    def recognize(self, context):
        buffer = context.image_stream.read()  # Reading the whole image stream
        if pytesseract is None:
            print("pytesseract is not installed: an image of %d bytes is not recognized" % len(buffer))
            return None
        with Image.open(io.BytesIO(buffer)) as image:
            recognized_text = pytesseract.image_to_string(image, lang="eng")
        return recognized_text


# Creating an index
index = Index("./index")

# Setting the OCR indexing options
options = IndexingOptions()
options.ocr_indexing_options.enabled_for_separate_images = True
options.ocr_indexing_options.ocr_connector = TesseractOcrConnector()

# Indexing documents in a document folder
index.add("./documents", options)