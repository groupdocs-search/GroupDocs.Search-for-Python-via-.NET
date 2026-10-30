from groupdocs.search import Index

# Creating an index and adding documents in separate operations, which creates several segments
index = Index("./index")
index.add("./documents/einstein-notes.txt")
index.add("./documents/newton.txt")
index.add("./documents/curie.txt")


# Subscribing to the event
def on_optimization_progress_changed(sender, args):
    print("Processed segments:", args.processed_segments)
    print("Total segments:", args.total_segments)
    print("Progress percentage:", args.progress_percentage)


index.events.optimization_progress_changed += on_optimization_progress_changed

# Optimizing the index
index.optimize()