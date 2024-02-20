class Magazine:
    _all_magazines = []  # Class variable to store all Magazine instances

    def __init__(self, name, category):
        # Initializes a Magazine with a given name and category.
        self._name = name
        self._category = category
        self._contributors = []  # List to store Author instances who have written for this magazine
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        # Returns the name of the magazine.
        return self._name

    @property
    def category(self):
        # Returns the category of the magazine.
        return self._category

    def contributing_authors(self, author):
        # Adds an Author instance to the list of contributors for this magazine.
        if author not in self._contributors:
            self._contributors.append(author)

    def contributors(self):
        # Returns a list of Author instances who have written for this magazine.
        return self._contributors

    @classmethod
    def all(cls):
        # Returns a list of all Magazine instances.
        return cls._all_magazines