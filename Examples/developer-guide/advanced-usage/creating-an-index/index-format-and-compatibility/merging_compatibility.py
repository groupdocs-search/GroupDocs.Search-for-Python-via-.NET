from groupdocs.search import Index, IndexSettings
from groupdocs.search.options import MergeOptions

# The new index divides text into terms as the previous versions did
settings = IndexSettings()
settings.replace_unpaired_surrogates = False
settings.skip_blended_only_terms = False

index = Index("./index", settings, True)
index.add("./documents")

updated_index = Index("./updated-index")  # An index updated from a previous version
try:
    index.merge(updated_index, MergeOptions())
    print("Indexed documents after merging:", len(index.get_indexed_documents()))
except RuntimeError as exception:
    # The indexes divide text into terms differently, for example, they use different alphabets;
    # the message names the differences
    print(exception.message)