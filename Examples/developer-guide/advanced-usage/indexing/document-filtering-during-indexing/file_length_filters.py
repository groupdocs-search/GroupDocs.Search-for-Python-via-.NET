from groupdocs.search.options import DocumentFilter

# The first filter skips documents less than 50 KB in length
filter1 = DocumentFilter.create_file_length_lower_bound(50 * 1024)

# The second filter skips documents more than 10 MB in length
filter2 = DocumentFilter.create_file_length_upper_bound(10 * 1024 * 1024)

# The third filter skips documents less than 100 KB and more than 5 MB in length
filter3 = DocumentFilter.create_file_length_range(100 * 1024, 5 * 1024 * 1024)

print(filter1)
print(filter2)
print(filter3)