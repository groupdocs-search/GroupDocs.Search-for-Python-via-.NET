from groupdocs.search import Index
from groupdocs.search.dictionaries import AliasReplacementPair

# Creating or opening an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

aliases = index.dictionaries.alias_dictionary

if aliases.count > 0:
    # Deleting all existing aliases
    aliases.clear()

# Adding aliases to the alias dictionary
aliases.add("t", "(theory OR relativity)")
aliases.add("e", "(Einstein OR Albert)")
pairs = [
    AliasReplacementPair("d", "daterange(2017-01-01 ~~ 2019-12-31)"),
    AliasReplacementPair("n", "(100 ~~ 900)"),
]
aliases.add_range(pairs)

if aliases.contains("e"):
    # Getting an alias replacement
    replacement = aliases.get_text("e")
    print("e - " + replacement)

# Exporting aliases to a file
aliases.export_dictionary("./Aliases.dat")

# Importing aliases from a file
aliases.import_dictionary("./Aliases.dat")

# Searching in the index
result = index.search("@t OR @e")
print("Documents found:", result.document_count)