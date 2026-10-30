from groupdocs.search import Index, IndexUpdater
from groupdocs.search.common import VersionUpdateResult

source_index_folder = "./old-index"
target_index_folder = "./new_index"

updater = IndexUpdater()

if updater.is_latest_version(source_index_folder):
    # The index has the current version and can be opened without updating
    index = Index(source_index_folder)
    print("The index has the current version")
elif updater.can_update_version(source_index_folder):
    # The index of the old version does not change
    result = updater.update_version(source_index_folder, target_index_folder)
    if result == VersionUpdateResult.UPDATED:
        # Opening the updated index
        index = Index(target_index_folder)
        print("The index is updated: " + str(len(index.get_indexed_documents())) + " documents")