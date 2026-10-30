import datetime
import os
import sys

from groupdocs.search import Index
from groupdocs.search.options import IndexingOptions

# The index starts the extraction service as an executable file,
# so a launcher runs extraction_service.py with this Python interpreter
service_path = os.path.abspath("./extraction_service.py")
if os.name == "nt":
    launcher_path = os.path.abspath("./extraction_service.cmd")
    with open(launcher_path, "w") as f:
        f.write('@"%s" "%s" %%*\n' % (sys.executable, service_path))
else:
    launcher_path = os.path.abspath("./extraction_service.sh")
    with open(launcher_path, "w") as f:
        f.write('#!/bin/sh\nexec "%s" "%s" "$@"\n' % (sys.executable, service_path))
    os.chmod(launcher_path, 0o755)

# Creating an index in the specified folder
index = Index("./index")

# Setting indexing options for data extraction in a separate process
options = IndexingOptions()
options.separate_process_options.extract_in_separate_process = True
options.separate_process_options.assembly_path = launcher_path
options.separate_process_options.use_dotnet_to_start_process = False
options.separate_process_options.timeout = datetime.timedelta(minutes=1)

# Indexing documents from the specified folder
index.add("./documents", options)

result = index.search("Einstein")
print("Documents found:", result.document_count)