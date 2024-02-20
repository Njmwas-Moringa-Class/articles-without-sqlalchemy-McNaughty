class Article:
    _all_articles = []  # Class variable to store all Article instances

    def __init__(self, author, magazine, title):
        # Initializes an Article with an author, a magazine, and a title.
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all_articles.append(self)

    @property
    def title(self):
        # Returns the title of the article.
        return self._title

    @property
    def author(self):
        # Returns the author of the article.
        return self._author

    @property
    def magazine(self):
        # Returns the magazine of the article.
        return self._magazine

    @classmethod
    def all(cls):
        # Returns a list of all Article instances.
        return cls._all_articles