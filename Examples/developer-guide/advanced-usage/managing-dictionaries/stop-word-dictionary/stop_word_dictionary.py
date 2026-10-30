from groupdocs.search import Index, IndexSettings

# Creating an index settings instance
settings = IndexSettings()
settings.use_stop_words = True  # Enabling the use of stop words during indexing

# Creating a new index in the specified folder; the dictionary can be changed only while the index contains no documents
index = Index("./index", settings, True)

stop_words = index.dictionaries.stop_word_dictionary

if stop_words.count > 0:
    # Removing all words from the dictionary
    stop_words.clear()

# Adding stop words to the dictionary
words = ["a", "an", "the", "but", "by"]
stop_words.add_range(words)

# The letter case of words is ignored
if stop_words.contains("But") and stop_words.contains("BY"):
    # Removing words from the dictionary
    stop_words.remove_range(["but", "by"])

# Exporting words to a file
stop_words.export_dictionary("./StopWords.txt")

# Importing words from a file
stop_words.import_dictionary("./StopWords.txt")
print("Stop words:", stop_words.count)

# Indexing documents; after that, the stop words of the index cannot be changed
index.add("./documents")