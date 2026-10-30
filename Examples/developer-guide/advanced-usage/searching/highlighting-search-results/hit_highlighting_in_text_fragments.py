import os

from groupdocs.search import Index, IndexSettings
from groupdocs.search.highlighters import FragmentHighlighter
from groupdocs.search.options import Color, Compression, HighlightOptions, OutputFormat, TextStorageSettings

# Creating an index settings instance
settings = IndexSettings()
settings.text_storage_settings = TextStorageSettings(Compression.HIGH)  # Enabling storage of extracted text in the index

# Creating an index in the specified folder
index = Index("./index", settings)

# Indexing documents from the specified folder
index.add("./documents")

# Search for the word 'Einstein'
result = index.search("Einstein")

# Assigning highlight options
options = HighlightOptions()
options.terms_before = 5
options.terms_after = 5
options.terms_total = 15
options.highlight_color = Color(0, 0, 127)
options.use_inline_styles = True

if result.document_count > 0:
    # Highlighting found words in separate text fragments of a document
    document = result.get_found_document(0)  # Getting the first found document
    highlighter = FragmentHighlighter(OutputFormat.HTML)
    index.highlight(document, highlighter, options)

    # Getting the result
    os.makedirs("./output", exist_ok=True)
    with open("./output/Fragments.html", "w", encoding="utf-8") as file:
        fragment_containers = highlighter.get_result()
        for container in fragment_containers:
            fragments = container.get_fragments()
            if len(fragments) > 0:
                print(container.field_name)
                print()
                for fragment in fragments:
                    # Printing HTML markup to console and saving it to the file
                    print(fragment)
                    print()
                    file.write("<p>" + fragment + "</p>\n")