import datetime
import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import DocumentField


class LogExtractor(object):
    extensions = [".log"]

    def get_fields(self, source):
        if isinstance(source, str):
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(source))
            return [
                DocumentField("FileName", os.path.abspath(source)),
                DocumentField("CreationDate", creation_time.strftime("%m/%d/%Y %H:%M:%S")),
                DocumentField("Content", self.extract_content(source)),
            ]
        return [DocumentField("Content", source.read().decode("utf-8-sig"))]

    def extract_content(self, file_path):
        with open(file_path, encoding="utf-8-sig") as f:
            return f.read()


settings = IndexSettings()
settings.custom_extractors.add(LogExtractor())  # Adding custom text extractor to the index settings

index = Index("./index", settings)  # Creating or loading an index

index.add("./documents")  # Indexing documents from the specified folder

result = index.search("quota")  # Searching for a word from the log file
print("Documents found:", result.document_count)