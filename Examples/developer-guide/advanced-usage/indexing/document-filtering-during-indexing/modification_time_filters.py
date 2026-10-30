import datetime

from groupdocs.search.options import DocumentFilter

# The first filter skips files modified earlier than January 1, 2017, 00:00:00
filter1 = DocumentFilter.create_modification_time_lower_bound(datetime.datetime(2017, 1, 1))

# The second filter skips files modified later than June 15, 2018, 00:00:00
filter2 = DocumentFilter.create_modification_time_upper_bound(datetime.datetime(2018, 6, 15))

# The third filter skips files modified outside the range from January 1, 2017, 00:00:00 to June 15, 2018, 00:00:00
filter3 = DocumentFilter.create_modification_time_range(datetime.datetime(2017, 1, 1), datetime.datetime(2018, 6, 15))

print(filter1)
print(filter2)
print(filter3)