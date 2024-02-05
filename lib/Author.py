class Author:
    def __init__(self, name):
        # Initializes an Author with a given name.
        self._name = name

    def name(self):
        # Returns the name of the author.
        return self._name