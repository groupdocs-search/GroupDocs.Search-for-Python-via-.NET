from groupdocs.search import Index, IndexSettings


class ConsoleLogger(object):
    def error(self, message):
        print("Error: " + message)

    def trace(self, message):
        print(message)


settings = IndexSettings()
settings.logger = ConsoleLogger()  # Assigning the custom logger

index = Index("./index", settings)  # Creating or loading an index from the specified folder