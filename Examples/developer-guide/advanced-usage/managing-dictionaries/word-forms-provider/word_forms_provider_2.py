from groupdocs.search import Index
from groupdocs.search.options import SearchOptions


class SimpleWordFormsProvider:
    def get_word_forms(self, word):
        result = []
        lower_word = word.lower()

        # We assume that the input word is in the plural, then we add the singular
        if len(word) > 3 and lower_word.endswith("ies"):
            result.append(word[:-3] + "y")
        if len(word) > 2 and lower_word.endswith("es"):
            result.append(word[:-2])
        if len(word) > 1 and lower_word.endswith("s"):
            result.append(word[:-1])

        # Then we assume that the input word is in the singular, we add the plural
        if len(word) > 1 and lower_word.endswith("y"):
            result.append(word[:-1] + "ies")
        elif lower_word.endswith(("s", "x", "ch", "sh")):
            result.append(word + "es")
        else:
            result.append(word + "s")

        return result


# Creating or opening an index in the specified folder
index = Index("./index")

# Indexing documents from the specified folder
index.add("./documents")

# Setting the custom word forms provider instance
index.dictionaries.word_forms_provider = SimpleWordFormsProvider()

# Creating a search options instance
options = SearchOptions()
options.use_word_forms_search = True  # Enabling search for word forms

# Searching in the index
result = index.search("relative", options)

# The following words can be found:
# relative
# relatives
for document in result:
    print(document.document_info.file_path)
    print("\tFound words:", ", ".join(document.terms))