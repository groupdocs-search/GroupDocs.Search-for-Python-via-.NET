import datetime
import os

from groupdocs.search.common import DocumentField


class LogExtractor(object):
    extensions = [".log"]

    def get_fields(self, source):
        if isinstance(source, str):
            # The document is a file: source is the path to the file
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(source))
            return [
                DocumentField("FileName", os.path.abspath(source)),
                DocumentField("CreationDate", creation_time.strftime("%m/%d/%Y %H:%M:%S")),
                DocumentField("Content", self.extract_content(source)),
            ]
        # The document is a stream: source.read() returns its bytes
        # The stream belongs to the caller, so it is not closed here
        return [DocumentField("Content", source.read().decode("utf-8-sig"))]

    def extract_content(self, file_path):
        with open(file_path, encoding="utf-8-sig") as f:
            return f.read()