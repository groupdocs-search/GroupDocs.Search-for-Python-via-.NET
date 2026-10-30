from groupdocs.search import Index, IndexUpdater
from groupdocs.search.common import VersionUpdateResult

index_folder = "./old-index"  # The folder of an existing index, here one created by a previous version
updated_index_folder = "./updated-index"  # A new empty folder for the updated index

updater = IndexUpdater()
if updater.is_latest_version(index_folder):
    # The index has the current version and can be opened as is
    index = Index(index_folder)
    print("The index has the current version.")
elif updater.can_update_version(index_folder):
    # The index of a previous version is converted or re-indexed into the new folder;
    # the source index is not changed
    result = updater.update_version(index_folder, updated_index_folder)
    if result != VersionUpdateResult.UPDATED:
        raise RuntimeError("The index cannot be updated: " + result.name)
    index = Index(updated_index_folder)
    print("The index has been updated.")
else:
    # The folder does not contain an index that can be opened or updated, so a new index is created
    index = Index(index_folder, True)
    print("A new index has been created.")

print("Indexed documents:", len(index.get_indexed_documents()))