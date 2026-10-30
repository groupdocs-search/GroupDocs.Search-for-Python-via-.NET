from groupdocs.search import Index

# Creating or opening an index in the specified folder
index = Index("./index")

homophones = index.dictionaries.homophone_dictionary

# Getting homophones for the word 'braid'; the letter case of the word is ignored
words = homophones.get_homophones("Braid")
print("Homophones for 'braid':")
for word in words:
    print(word)

# Getting groups of homophones to which the word 'braid' belongs
groups = homophones.get_homophone_groups("braid")
print("Homophone groups for 'braid':")
for group in groups:
    print(" ".join(group))

if homophones.count > 0:
    # Removing all homophones from the dictionary
    homophones.clear()

# Adding homophones to the dictionary
homophone_groups = [
    ["awe", "oar", "or", "ore"],
    ["aye", "eye", "i"],
]
homophones.add_range(homophone_groups)
print("Words in the dictionary:", homophones.count)

# Exporting homophones to a file
homophones.export_dictionary("./Homophones.dat")

# Importing homophones from a file
homophones.import_dictionary("./Homophones.dat")