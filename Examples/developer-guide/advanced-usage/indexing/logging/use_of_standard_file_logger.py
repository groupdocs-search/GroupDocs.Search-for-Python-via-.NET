import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.common import FileLogger

query = "Einstein"
log_path = "./output/log.txt"
os.makedirs("./output", exist_ok=True)

settings = IndexSettings()
settings.logger = FileLogger(log_path, 4.0)  # Specifying the path to the log file and a maximum length of 4 MB

index = Index("./index", settings)  # Creating or loading an index from the specified folder

index.add("./documents")  # Indexing documents from the specified folder

result = index.search(query)  # Search in index

with open(log_path, encoding="utf-8") as f:
    print(f.read())