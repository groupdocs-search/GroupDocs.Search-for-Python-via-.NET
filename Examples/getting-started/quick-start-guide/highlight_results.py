import os

from groupdocs.search import Index, License
from groupdocs.search.highlighters import FragmentHighlighter
from groupdocs.search.options import HighlightOptions, OutputFormat

def highlight_results():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Search.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    with Index("./index") as index:
        index.add("./documents")
        result = index.search("gravity")

        # Four words of context on each side of a found word, which is put in brackets
        options = HighlightOptions()
        options.terms_before = 4
        options.terms_after = 4
        options.term_highlight_start_tag = "["
        options.term_highlight_end_tag = "]"

        for document in sorted(result, key=lambda found: found.relevance, reverse=True):
            highlighter = FragmentHighlighter(OutputFormat.PLAIN_TEXT)
            index.highlight(document, highlighter, options)
            print(os.path.basename(document.document_info.file_path))
            for container in highlighter.get_result():
                for fragment in container.get_fragments():
                    print("   ", " ".join(fragment.split()))

if __name__ == "__main__":
    highlight_results()