import re

from groupdocs.search import Index

try:
    import jieba  # pip install jieba
except ImportError:
    jieba = None


# Implementing custom word splitter
class JiebaWordSplitter(object):
    def split(self, text):
        if jieba is not None:
            return jieba.lcut(text, cut_all=False)
        # Without jieba: each run of ideographs is split into overlapping two-character words
        words = []
        for run in re.findall("[\u4e00-\u9fff]+|\\w+", text):
            if "\u4e00" <= run[0] <= "\u9fff" and len(run) > 1:
                words.extend(run[i:i + 2] for i in range(len(run) - 1))
            else:
                words.append(run)
        return words


# Creating an index in the specified folder
index = Index("./index")

# Using Jieba segmenter to break text into words
jieba_word_splitter = JiebaWordSplitter()


def on_file_indexing(sender, args):
    if args.document_full_path.endswith("Chinese.txt"):
        # We know that the text in this document is in Chinese
        args.word_splitter = jieba_word_splitter


index.events.file_indexing += on_file_indexing

# Indexing documents
index.add("./documents")

# Searching in the index
query = "考虑"  # Consider
result = index.search(query)
print("Documents found:", result.document_count)