from groupdocs.search import Index, IndexSettings

# Creating index settings
settings = IndexSettings()
settings.skip_blended_only_terms = False  # Keeping the terms consisting only of blended characters

# Creating an index with the specified settings
index = Index("./index", settings, True)

# Indexing documents from the specified folder
index.add("./documents")

print("Skip blended-only terms:", index.index_settings.skip_blended_only_terms)