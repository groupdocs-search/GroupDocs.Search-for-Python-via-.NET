import os

from groupdocs.search import Index

# Creating or opening an index in the specified folder
index = Index("./index")

passwords = index.dictionaries.document_passwords

path = os.path.abspath("./documents/protected.pdf")
if passwords.contains(path):
    # Getting a password for a document
    password = passwords.get_password(path)
    print(path)
    print("\tPassword: " + password)

    # Deleting the password from the dictionary
    passwords.remove(path)

if passwords.count > 0:
    # Removing all passwords from the dictionary
    passwords.clear()

# Adding a password for a document
passwords.add(path, "123456")

# Exporting passwords to a file
passwords.export_dictionary("./Passwords.dat")

# Removing all passwords and importing them from the file
passwords.clear()
passwords.import_dictionary("./Passwords.dat")

# Indexing documents; the passwords from the dictionary are used to open protected documents
index.add("./documents")

# Searching for a word of the protected document
result = index.search("confidential")
print("Documents found:", result.document_count)