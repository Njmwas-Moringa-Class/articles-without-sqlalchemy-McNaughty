class Magazine:
    _all_magazines = []  # Class variable to store all Magazine instances

    def __init__(self, name, category):
        # Initializes a Magazine with a given name and category.
        self._name = name
        self._category = category
        Magazine._all_magazines.append(self)

    def get_name(self):
        # Returns the name of the magazine.
        return self._name

    def get_category(self):
        # Returns the category of the magazine.
        return self._category

    @classmethod
    def all(cls):
        # Returns a list of all Magazine instances.
        return cls._all_magazines