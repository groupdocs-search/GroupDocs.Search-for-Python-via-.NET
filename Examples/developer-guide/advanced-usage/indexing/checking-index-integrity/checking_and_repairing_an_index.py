from groupdocs.search import Index

# Opening an existing index
index = Index("./index")

# Collecting the messages about damage and repair
messages = []
index.events.error_occurred += lambda sender, args: messages.append(args.message)

# Checking the index without changing it
index.check_segments(False)

if len(messages) > 0:
    for message in messages:
        print(message)

    # Repairing the index
    messages.clear()
    index.check_segments(True)
    for message in messages:
        print(message)

    # Indexing again the files of the documents deleted by the repair
    index.update()
else:
    print("No damage found: the index is intact.")