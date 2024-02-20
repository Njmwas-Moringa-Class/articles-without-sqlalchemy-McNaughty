from Article import Article
from Magazine import Magazine

class Author:
    _all_authors = []  # List to store all Author instances

    def __init__(self, name):
        # Initializes an Author with a given name.
        self._name = name
        self._articles = []  # List to store Article instances by this author
        Author._all_authors.append(self)

    @property
    def name(self):
        # Returns the name of the author.
        return self._name

    def add_article(self, magazine, title):
        # creates a new Article instance and associates it with that author and that magazine.
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)

    def articles(self):
        # Returns a list of Article instances written by the author.
        return self._articles

    def magazines(self):
        # Returns a unique list of Magazine instances for which the author has contributed.
        return list(set(article.magazine for article in self._articles))

    @classmethod
    def all(cls):
        # Returns a list of all Author instances.
        return cls._all_authors

    def topic_areas(self):
        # Returns the topic areas of the author (for example, based on their articles or other data).
        return ["Coding", "Finance"] 
