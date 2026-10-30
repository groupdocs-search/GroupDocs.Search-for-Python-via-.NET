from groupdocs.search import Index

index = Index("./index")

def on_error_occurred(sender, args):
    print(args.message)  # Writing error messages to the console

index.events.error_occurred += on_error_occurred

index.add("./documents")