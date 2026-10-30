from groupdocs.search import Extractor, Index
from groupdocs.search.common import Document, ExtractedData
from groupdocs.search.options import ExtractionOptions, IndexingOptions

document_path = "./sample.pdf"

# Extracting data from a document
extractor = Extractor()
extractor.error_occurred += lambda sender, args: print(args.message)
document = Document.create_from_file(document_path)
extraction_options = ExtractionOptions()
extraction_options.use_raw_text_extraction = False
extracted_data = extractor.extract(document, extraction_options)

# Serializing the data
array = extracted_data.serialize()

# Deserializing the data
deserialized_data = ExtractedData.deserialize(array)

# Creating an index
index = Index("./index")

if deserialized_data.is_extraction_successful:
    # Indexing the data
    data = [
        deserialized_data
    ]
    index.add(data, IndexingOptions())

    # Searching in the index
    result = index.search("Einstein")
    print("Documents found:", result.document_count)