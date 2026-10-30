from groupdocs.search import RegexOptions
from groupdocs.search.options import DocumentFilter

# The filter skips files that do not contain the word 'Einstein' in their paths, not case sensitive
document_filter = DocumentFilter.create_file_path_regular_expression("Einstein", RegexOptions.IGNORE_CASE)

print(document_filter)