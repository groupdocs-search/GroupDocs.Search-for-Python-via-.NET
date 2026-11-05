# GroupDocs.Search for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-search-python-net-banner.png)](https://releases.groupdocs.com/search/python-net/)

[Product Page](https://products.groupdocs.com/search/python-net/) | [Docs](https://docs.groupdocs.com/search/python-net/) | [Demos](https://products.groupdocs.app/search/family) | [API Reference](https://reference.groupdocs.com/search/python-net/) | [Blog](https://blog.groupdocs.com/category/search/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/search/) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Search for Python via .NET](https://products.groupdocs.com/search/python-net/) is a full-text search and indexing API: build a persistent, disk-backed index over a folder of documents and run keyword, phrase, wildcard, regular-expression, fuzzy, boolean, faceted, synonym, and homophone queries against Word, Excel, PowerPoint, PDF, email, eBook, web, and plain-text formats — entirely on-premise, with no Microsoft Office or other external software required.

## Features

- **Persistent Indexing**: Build a disk-backed index over files or folders and reopen it across runs; `update()` re-indexes only what changed.
- **Rich Query Language**: Keyword, phrase, wildcard, regular-expression, boolean, and faceted queries from a single text query.
- **Fuzzy Search**: Tolerate typos and OCR noise with a configurable similarity level.
- **Synonym, Homophone & Word-Forms Search**: Expand a query through built-in or custom dictionaries.
- **Highlighting**: Render whole-document or fragment highlights of matches to HTML or plain text.
- **Index Maintenance**: Update, optimize, merge, and delete documents, and inspect indexing and search reports.
- **On-Premise**: No MS Office or OpenOffice installation required.

## Supported File Formats

GroupDocs.Search for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, Email, eBook, Markup, Archive, Image, and many others. See the [full list of supported formats](https://docs.groupdocs.com/search/python-net/supported-document-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.5+](https://www.python.org/downloads/) is installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-search/GroupDocs.Search-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Search-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/search/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_search_net-26.10.0-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: `run_all_examples.py` applies a license automatically when the `GROUPDOCS_LIC_PATH` environment variable holds the absolute path of your `.lic` file.

   With a license applied, examples run with the full feature set; without one, an index takes at most 100 documents, and only the first 10 found documents of a search can be read. Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the system packages the examples need (`libicu-dev`, `libgdiplus`), and the `groupdocs-search-net` package preinstalled.

```bash
# Build the image
docker build -t search-examples .

# Run unlicensed (evaluation mode)
docker run --rm search-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    search-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-search-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/search/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting.

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/search/python-net/agents-and-llm-integration/) page for the per-tool setup snippets.

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Search for Python via .NET documentation](https://docs.groupdocs.com/search/python-net/).

We also offer **GroupDocs.Search** packages for other platforms:
* [**GroupDocs.Search for .NET**](https://products.groupdocs.com/search/net/)
* [**GroupDocs.Search for Java**](https://products.groupdocs.com/search/java/)
* [**GroupDocs.Search for Node.js via Java**](https://products.groupdocs.com/search/nodejs-java/)

---

[Product Page](https://products.groupdocs.com/search/python-net/) | [Docs](https://docs.groupdocs.com/search/python-net/) | [Demos](https://products.groupdocs.app/search/family) | [API Reference](https://reference.groupdocs.com/search/python-net/) | [Blog](https://blog.groupdocs.com/category/search/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/search/) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
