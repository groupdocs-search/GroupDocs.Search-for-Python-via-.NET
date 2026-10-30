import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import DocumentField, ExtractedItemInfo
from groupdocs.search.results import FormatFamily


class LineContainerExtractor(object):
    extensions = [".lines"]
    format_family = FormatFamily.ARCHIVE

    def get_fields(self, source):
        if isinstance(source, str):
            # The container document itself has only the file name field
            return [DocumentField("FileName", os.path.basename(source))]
        return []

    def get_container_items(self, source):
        if isinstance(source, str):
            with open(source, encoding="utf-8-sig") as f:
                lines = f.read().splitlines()
        else:
            lines = source.read().decode("utf-8-sig").splitlines()
        return self.create_items(lines)

    @staticmethod
    def create_items(lines):
        items = []
        for i, line in enumerate(lines):
            fields = [DocumentField("Content", line)]
            item_info = "Line " + str(i + 1)
            items.append(ExtractedItemInfo(FormatFamily.WORD_PROCESSING, fields, item_info, ""))
        return items


# Indexing the lines of the .lines files as separate items
settings = IndexSettings()
settings.custom_extractors.add(LineContainerExtractor())
index = Index("./index", settings)
index.add("./documents")

# Getting the indexed items of each container document
for document in index.get_indexed_documents():
    print(os.path.basename(document.file_path))
    for item in index.get_indexed_document_items(document):
        print("\t" + item.inner_path)

# Searching in the items
result = index.search("Venus")
for found in result:
    print("Found in:", found.document_info.inner_path)