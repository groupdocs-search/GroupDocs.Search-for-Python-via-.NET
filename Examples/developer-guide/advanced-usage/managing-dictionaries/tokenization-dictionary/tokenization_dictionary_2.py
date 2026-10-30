from groupdocs.search import Index
from groupdocs.search.dictionaries import CharacterType


# A simple word splitter that divides text into words at white space characters
class WhiteSpaceWordSplitter:
    def split(self, text):
        return text.split()


# Creating a new index in the specified folder;
# the tokenization dictionary can be changed only while the index contains no documents
index = Index("./index", True)

tokenization_dictionary = index.dictionaries.tokenization_dictionary

# Getting the type of a Hiragana character, which is a separator by default
print("The type of U+3042:", tokenization_dictionary.get_character_type("あ").name)

# Setting the Letter type for Hiragana and Katakana characters
code_points = list(range(0x3040, 0x3100))
tokenization_dictionary.set_range(code_points, CharacterType.LETTER)

# Getting the number of characters that are not separators
print("Characters that are not separators:", tokenization_dictionary.count)

# Exporting the tokenization dictionary to a file, for example, to use it in other indexes
tokenization_dictionary.export_dictionary("./TokenizationDictionary.dat")

# Using the custom word splitter for text documents
word_splitter = WhiteSpaceWordSplitter()


def on_file_indexing(sender, args):
    if args.document_full_path.lower().endswith(".txt"):
        args.word_splitter = word_splitter


index.events.file_indexing += on_file_indexing

# Indexing documents; after that, the tokenization dictionary of the index cannot be changed
index.add("./documents")

# Searching for a Hiragana word
result = index.search("ひらがな")
print("Documents found:", result.document_count)