class ConsoleLogger(object):
    def error(self, message):
        print("Error: " + message)

    def trace(self, message):
        print(message)