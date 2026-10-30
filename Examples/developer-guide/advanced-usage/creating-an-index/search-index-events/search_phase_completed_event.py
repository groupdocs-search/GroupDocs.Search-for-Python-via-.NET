from groupdocs.search import Index
from groupdocs.search.options import SearchOptions

# Creating an index
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")


# Subscribing to the event
def on_search_phase_completed(sender, args):
    words = args.words
    print("Search phase:", args.search_phase.name)
    print("Words:", len(words))
    for word in words:
        print("\t" + word)
    print()


index.events.search_phase_completed += on_search_phase_completed

options = SearchOptions()
options.use_synonym_search = True
options.use_word_forms_search = True
options.fuzzy_search.enabled = True
options.use_homophone_search = True
result = index.search("Einstein", options)