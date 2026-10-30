from groupdocs.search import Index, IndexUpdater
from groupdocs.search.common import VersionUpdateResult

index_folder = "./old-index"  # The folder of an index created by a previous version
updated_index_folder = "./updated-index"  # A new empty folder for the updated index

updater = IndexUpdater()
if updater.can_update_version(index_folder):
    # The source index is not changed; the content of the target folder is deleted before the update
    result = updater.update_version(index_folder, updated_index_folder)
    if result == VersionUpdateResult.UPDATED:
        with Index(updated_index_folder) as index:
            search_result = index.search("Einstein")
            print("Documents found:", search_result.document_count)