# extraction_service.py
import sys

from groupdocs.search import ExtractionHost

# The index starts this script and passes the name of the communication channel
with ExtractionHost(sys.argv[1:]) as host:
    host.run()