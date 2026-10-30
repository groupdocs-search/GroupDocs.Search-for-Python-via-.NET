import os
import sys
import traceback

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# output that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Search for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to build an index, add documents, search, and highlight results with GroupDocs.Search.
Each example demonstrates different use cases and functionalities such as:

- Creating a persistent on-disk index and an in-memory index.
- Adding documents from files and folders.
- Keyword, phrase, wildcard, regular-expression, boolean, and faceted search.
- Fuzzy, case-sensitive, synonym, homophone, and word-forms search.
- Highlighting matches in whole documents and fragments.
- Updating, optimizing, and deleting documents from an index.
- Inspecting indexing and search reports.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.search import License

    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        try:
            License().set_license(license_path)
            print(GREEN + "License set from: " + license_path + RESET + "\n")
        except Exception as exc:
            print(YELLOW + "Could not apply license ({}). Running in evaluation mode.".format(exc) + RESET + "\n")
    else:
        print(YELLOW + "No license file found. Running in evaluation mode." + RESET + "\n")

def run_example(base_dir, example_path):
    """Run a single example by executing its script in-process."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)
    saved_cwd = os.getcwd()
    os.chdir(example_dir)
    try:
        code = open(full_path, "r", encoding="utf-8").read()
        exec(compile(code, full_path, "exec"), {"__name__": "__main__", "__file__": full_path})
    finally:
        os.chdir(saved_cwd)

examples = [
    "getting-started/hello-world/hello_world.py",
    "getting-started/quick-start-guide/search_documents.py",
    "getting-started/quick-start-guide/fuzzy_search.py",
    "getting-started/quick-start-guide/highlight_results.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "licensing/searching_limitations.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_1_create_new_index.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_2_open_existing_index.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_3_subscribe_to_index_events.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_4_add_files_synchronously.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_5_add_files_asynchronously.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_6_perform_search.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_7_use_search_results.py",
    "developer-guide/basic-usage/build-your-first-search-solution/step_7_use_search_results_2.py",
    "developer-guide/basic-usage/build-search-query/build_search_query.py",
    "developer-guide/basic-usage/build-search-query/simple_search_query.py",
    "developer-guide/basic-usage/build-search-query/wildcard_search_query.py",
    "developer-guide/basic-usage/build-search-query/wildcard_search_query_2.py",
    "developer-guide/basic-usage/build-search-query/faceted_search_query.py",
    "developer-guide/basic-usage/build-search-query/numeric_range_search_query.py",
    "developer-guide/basic-usage/build-search-query/date_range_search_query.py",
    "developer-guide/basic-usage/build-search-query/regular_expression_search_query.py",
    "developer-guide/basic-usage/build-search-query/boolean_search_query.py",
    "developer-guide/basic-usage/build-search-query/boolean_search_query_2.py",
    "developer-guide/basic-usage/build-search-query/phrase_search_query.py",
    "developer-guide/basic-usage/work-with-search-results/obtain_search_result_information.py",
    "developer-guide/basic-usage/work-with-search-results/highlight_search_results.py",
    "developer-guide/basic-usage/get-supported-file-formats/get_supported_file_formats.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-location/search_index_location.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-location/search_index_location_2.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/operation_finished_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/error_occurred_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/operation_progress_changed_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/optimization_progress_changed_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/password_required_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/file_indexing_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/status_changed_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/search_phase_completed_event.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-events/image_preparing_event.py",
    "developer-guide/advanced-usage/indexing/character-replacement-during-indexing/character_replacement_during_indexing.py",
    "developer-guide/advanced-usage/managing-dictionaries/alias-dictionary/alias_dictionary.py",
    "developer-guide/advanced-usage/searching/boolean-search/operator_and.py",
    "developer-guide/advanced-usage/searching/boolean-search/operator_or.py",
    "developer-guide/advanced-usage/searching/boolean-search/operator_not.py",
    "developer-guide/advanced-usage/searching/boolean-search/complex_queries.py",
    "developer-guide/advanced-usage/searching/boolean-search/complex_queries_2.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-repository/search_index_repository.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-repository/search_index_repository_2.py",
    "developer-guide/advanced-usage/indexing/character-types/regular_characters.py",
    "developer-guide/advanced-usage/indexing/character-types/blended_characters.py",
    "developer-guide/advanced-usage/indexing/character-types/indexing_each_character_as_a_whole_word.py",
    "developer-guide/advanced-usage/managing-dictionaries/alphabet/alphabet.py",
    "developer-guide/advanced-usage/managing-dictionaries/alphabet/alphabet_2.py",
    "developer-guide/advanced-usage/searching/case-sensitive-search/case_sensitive_search.py",
    "developer-guide/advanced-usage/searching/case-sensitive-search/case_sensitive_search_2.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-settings/search_threads_property.py",
    "developer-guide/advanced-usage/creating-an-index/search-index-settings/skip_blended_only_terms_property.py",
    "developer-guide/advanced-usage/indexing/checking-index-integrity/checking_and_repairing_an_index.py",
    "developer-guide/advanced-usage/managing-dictionaries/character-replacements/character_replacements.py",
    "developer-guide/advanced-usage/searching/date-range-search/creating_date_range_search_queries.py",
    "developer-guide/advanced-usage/searching/date-range-search/specifying_date_range_search_formats.py",
    "developer-guide/advanced-usage/searching/date-range-search/specifying_date_range_search_formats_2.py",
    "developer-guide/advanced-usage/creating-an-index/index-format-and-compatibility/updating_an_index_of_a_previous_version.py",
    "developer-guide/advanced-usage/creating-an-index/index-format-and-compatibility/merging_compatibility.py",
    "developer-guide/advanced-usage/indexing/custom-text-extractors/custom_text_extractors.py",
    "developer-guide/advanced-usage/indexing/custom-text-extractors/custom_text_extractors_2.py",
    "developer-guide/advanced-usage/indexing/custom-text-extractors/custom_extractors_for_container_documents.py",
    "developer-guide/advanced-usage/managing-dictionaries/document-passwords/document_passwords.py",
    "developer-guide/advanced-usage/searching/document-filtering-in-search-result/setting_a_filter.py",
    "developer-guide/advanced-usage/searching/document-filtering-in-search-result/file_path_filters.py",
    "developer-guide/advanced-usage/searching/document-filtering-in-search-result/file_extension_filter.py",
    "developer-guide/advanced-usage/searching/document-filtering-in-search-result/attribute_filter.py",
    "developer-guide/advanced-usage/searching/document-filtering-in-search-result/combining_filters.py",
    "developer-guide/advanced-usage/indexing/custom-text-segmenter/custom_text_segmenter.py",
    "developer-guide/advanced-usage/managing-dictionaries/homophone-dictionary/homophone_dictionary.py",
    "developer-guide/advanced-usage/searching/faceted-search/creating_faceted_search_queries.py",
    "developer-guide/advanced-usage/searching/faceted-search/creating_faceted_search_queries_2.py",
    "developer-guide/advanced-usage/searching/faceted-search/using_format_specific_fields.py",
    "developer-guide/advanced-usage/indexing/delete-indexed-documents/delete_indexed_documents.py",
    "developer-guide/advanced-usage/managing-dictionaries/spelling-corrector/spelling_corrector.py",
    "developer-guide/advanced-usage/searching/fuzzy-search/fuzzy_search_features.py",
    "developer-guide/advanced-usage/searching/fuzzy-search/fuzzy_search_features_2.py",
    "developer-guide/advanced-usage/indexing/delete-indexed-paths/delete_indexed_paths.py",
    "developer-guide/advanced-usage/managing-dictionaries/stop-word-dictionary/stop_word_dictionary.py",
    "developer-guide/advanced-usage/searching/getting-indexed-documents/getting_indexed_documents.py",
    "developer-guide/advanced-usage/searching/getting-indexed-documents/getting_indexed_documents_2.py",
    "developer-guide/advanced-usage/searching/getting-indexed-documents/getting_text_of_indexed_documents.py",
    "developer-guide/advanced-usage/indexing/document-attributes/document_attributes.py",
    "developer-guide/advanced-usage/indexing/document-attributes/document_attributes_2.py",
    "developer-guide/advanced-usage/managing-dictionaries/synonym-dictionary/synonym_dictionary.py",
    "developer-guide/advanced-usage/searching/highlighting-search-results/hit_highlighting_in_the_text_of_entire_document.py",
    "developer-guide/advanced-usage/searching/highlighting-search-results/hit_highlighting_in_text_fragments.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/setting_a_filter.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/creation_time_filters.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/modification_time_filters.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/file_path_filters.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/file_length_filters.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/file_extension_filter.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/logical_not_filter.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/logical_and_filter.py",
    "developer-guide/advanced-usage/indexing/document-filtering-during-indexing/logical_or_filter.py",
    "developer-guide/advanced-usage/managing-dictionaries/tokenization-dictionary/tokenization_dictionary.py",
    "developer-guide/advanced-usage/managing-dictionaries/tokenization-dictionary/tokenization_dictionary_2.py",
    "developer-guide/advanced-usage/managing-dictionaries/tokenization-dictionary/tokenization_dictionary_3.py",
    "developer-guide/advanced-usage/searching/homophone-search/homophone_search.py",
    "developer-guide/advanced-usage/indexing/document-renaming/document_renaming.py",
    "developer-guide/advanced-usage/managing-dictionaries/word-forms-provider/word_forms_provider.py",
    "developer-guide/advanced-usage/managing-dictionaries/word-forms-provider/word_forms_provider_2.py",
    "developer-guide/advanced-usage/searching/keyboard-layout-correction/keyboard_layout_correction.py",
    "developer-guide/advanced-usage/indexing/extraction-in-separate-process/extraction_in_separate_process.py",
    "developer-guide/advanced-usage/searching/nesting-search-queries-in-object-form/nesting_search_queries_in_object_form.py",
    "developer-guide/advanced-usage/indexing/indexing-additional-fields/indexing_additional_fields.py",
    "developer-guide/advanced-usage/searching/numeric-range-search/numeric_range_search.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_a_file.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_a_stream.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_a_structure.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_url.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_ftp.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_amazon_s3_storage.py",
    "developer-guide/advanced-usage/indexing/indexing-from-different-sources/indexing_from_azure_blob_storage.py",
    "developer-guide/advanced-usage/searching/output-adapters/output_adapters.py",
    "developer-guide/advanced-usage/indexing/indexing-metadata-of-documents/indexing_metadata_of_documents.py",
    "developer-guide/advanced-usage/searching/phrase-search/phrase_search_in_groupdocs_search.py",
    "developer-guide/advanced-usage/searching/phrase-search/phrase_search_with_wildcards.py",
    "developer-guide/advanced-usage/searching/phrase-search/phrase_search_with_wildcards_2.py",
    "developer-guide/advanced-usage/indexing/indexing-options/cancellation_property.py",
    "developer-guide/advanced-usage/indexing/indexing-options/is_async_property.py",
    "developer-guide/advanced-usage/indexing/indexing-options/threads_property.py",
    "developer-guide/advanced-usage/indexing/indexing-options/metadata_indexing_options_property.py",
    "developer-guide/advanced-usage/searching/queries-in-text-and-object-form/queries_in_text_and_object_form.py",
    "developer-guide/advanced-usage/indexing/indexing-password-protected-documents/indexing_using_the_password_dictionary.py",
    "developer-guide/advanced-usage/indexing/indexing-password-protected-documents/indexing_using_the_password_required_event.py",
    "developer-guide/advanced-usage/indexing/indexing-reports/indexing_reports.py",
    "developer-guide/advanced-usage/searching/regular-expression-search/regular_expression_search.py",
    "developer-guide/advanced-usage/searching/regular-expression-search/regular_expression_search_2.py",
    "developer-guide/advanced-usage/searching/reverse-image-search/reverse_image_search.py",
    "developer-guide/advanced-usage/indexing/indexing-with-stop-words/indexing_with_stop_words.py",
    "developer-guide/advanced-usage/searching/search-by-chunks/how_to_perform_search_by_chunks.py",
    "developer-guide/advanced-usage/searching/search-by-chunks/cancellation_of_search_by_chunks.py",
    "developer-guide/advanced-usage/indexing/logging/use_of_standard_file_logger.py",
    "developer-guide/advanced-usage/indexing/logging/implementing_custom_logger.py",
    "developer-guide/advanced-usage/indexing/logging/implementing_custom_logger_2.py",
    "developer-guide/advanced-usage/indexing/merge-indexes/merging_example.py",
    "developer-guide/advanced-usage/searching/search-for-different-word-forms/search_for_different_word_forms.py",
    "developer-guide/advanced-usage/searching/search-for-text-containing-special-characters/search_for_text_containing_special_characters.py",
    "developer-guide/advanced-usage/indexing/ocr-support/ocr_support.py",
    "developer-guide/advanced-usage/indexing/ocr-support/ocr_support_2.py",
    "developer-guide/advanced-usage/indexing/ocr-support/ocr_support_3.py",
    "developer-guide/advanced-usage/indexing/optimize-index/optimize_index.py",
    "developer-guide/advanced-usage/searching/search-options/retrieve_attributes_property.py",
    "developer-guide/advanced-usage/searching/search-options/incompatible_options.py",
    "developer-guide/advanced-usage/indexing/separate-data-extraction/separate_data_extraction.py",
    "developer-guide/advanced-usage/searching/search-reports/search_reports.py",
    "developer-guide/advanced-usage/indexing/storing-text-of-indexed-documents/storing_text_of_indexed_documents.py",
    "developer-guide/advanced-usage/searching/search-results/search_results.py",
    "developer-guide/advanced-usage/indexing/text-file-encoding-detection/text_file_encoding_detection.py",
    "developer-guide/advanced-usage/indexing/text-file-encoding-detection/text_file_encoding_detection_2.py",
    "developer-guide/advanced-usage/indexing/update-index/update_indexed_documents.py",
    "developer-guide/advanced-usage/indexing/update-index/update_index_version.py",
    "developer-guide/advanced-usage/searching/spell-checking/spell_checking.py",
    "developer-guide/advanced-usage/searching/synonym-search/synonym_search.py",
    "developer-guide/advanced-usage/searching/using-aliases/using_aliases.py",
    "developer-guide/advanced-usage/searching/wildcard-search/wildcard_search.py",
    "developer-guide/advanced-usage/searching/wildcard-search/wildcard_search_2.py",
    "developer-guide/migration-notes/opening_indexes_of_previous_versions.py",
    "developer-guide/migration-notes/term_dictionaries_are_fixed_once_an_index_contains_documents.py",
    "developer-guide/migration-notes/incompatible_indexes_are_not_merged.py",
    "developer-guide/migration-notes/search_is_multithreaded_by_default.py",
    "developer-guide/migration-notes/search_by_chunks_returns_a_different_number_of_chunks.py",
    "product-overview/quick_example.py",
    "product-overview/search_with_options.py",
]

print_intro()
set_license()

base_dir = os.path.dirname(os.path.abspath(__file__))
passed = 0
failed = 0

for example in examples:
    print(YELLOW + "Running " + example + "..." + RESET)
    try:
        run_example(base_dir, example)
        print(GREEN + "Completed " + example + RESET + "\n")
        passed += 1
    except Exception as e:
        print(RED + "Error in {}: {}: {}".format(example, type(e).__name__, e) + RESET + "\n")
        failed += 1

print("\n{}Passed: {}{}  {}Failed: {}{}  Total: {}".format(GREEN, passed, RESET, RED, failed, RESET, passed + failed))

sys.exit(1 if failed else 0)
