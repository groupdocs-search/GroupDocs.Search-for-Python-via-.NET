from groupdocs.search.results import FileType

supported_file_types = sorted(
    (ft for ft in FileType.get_supported_file_types() if ft != FileType.UNKNOWN),  # Skipping the unknown file type
    key=lambda ft: ft.extension)

for file_type in supported_file_types:
    print(file_type.extension.ljust(8) + " - " + file_type.description)