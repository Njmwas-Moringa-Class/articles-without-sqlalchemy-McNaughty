class Magazine:
    _all_magazines = []  # Class variable to store all Magazine instances

    def __init__(self, name, category):
        # Initializes a Magazine with a given name and category.
        self._name = name
        self._category = category
        self._contributing_authors = []  # List to store Author instances who have written for this magazine
        self._articles = []  # List to store Article instances associated with this magazine
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        # Returns the name of the magazine.
        return self._name

    @property
    def category(self):
        # Returns the category of the magazine.
        return self._category

    def add_contributor(self, author):
        # Adds an Author instance to the list of contributors for this magazine.
        if author not in self._contributors:
            self._contributors.append(author)

    def magazine_contributors(self):
        # Returns a list of Author instances who have contributed to this magazine.
        return self._contributors

    def add_article(self, article):
        # Adds an Article instance to the list of articles associated with this magazine.
        self._articles.append(article)

    def articles(self):
        # Returns a list of Article instances associated with this magazine.
        return self._articles

    def article_titles(self):
        # Returns a list of titles of articles associated with this magazine.
        return [article.title for article in self._articles]

    @classmethod
    def all(cls):
        # Returns a list of all Magazine instances.
        return cls._all_magazines

    @classmethod
    def find_by_name(cls, name):
        # Finds magazines by name.
        return [magazine for magazine in cls._all_magazines if magazine.name == name]
