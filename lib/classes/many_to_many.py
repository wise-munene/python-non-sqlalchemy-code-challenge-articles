class Article:
    #represents an article written by an author for a magazine
    all = []  # Class variable to store all articles
   
    def __init__(self, author, magazine, title):
        #represents an article written by an author for a magazine
        if not isinstance(title, str): # validates that title is a string
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
      
        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)  # Add the article to the class variable

    @property
    def title(self): #returns articles title
         return self._title
        
    @property
    def author(self): #returns articles authors
        return self._author
        
    @author.setter
    def author(self, value): #sets articles author
            from types import SimpleNamespace
            if not isinstance(value, Author):
                raise TypeError("Author must be an instance of Author")
            self._author = value


    @property
    def magazine(self): #returns articles magazine
            return self._magazine
        
    @magazine.setter
    def magazine(self, value): #sets articles magazine
            if not isinstance(value, Magazine):
                raise TypeError("Magazine must be an instance of Magazine")
            self._magazine = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str): # validates that author is an instance of Author
            raise TypeError("Name must be of type str")
        if len(name)==0: # validates that name is not empty
            raise ValueError("Name must be longer than 0 characters")
        self._name=name

    @property
    def name(self): #returns authors name
        return self._name
    
    @name.setter
    def name(self, value): #sets authors name
         pass

        
         
    def articles(self):  # returns a list of articles written by the author
        return [article for article in Article.all if article.author == self]

    def magazines(self):   # returns a list of unique magazines the author has written for
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):   # creates a new article written by the author for a magazine
        if not isinstance(magazine, Magazine):# validates that magazine is an instance of Magazine
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str): # validates that title is a string
            raise ValueError("Title must be a string")
        return Article(self, magazine, title)

    def topic_areas(self):
        # returns a set of unique categories of magazines the author has written for
        categories ={article.magazine.category for article in self.articles()}
        return list(categories) if categories else None


class Magazine:
    all_magazines = []  # Class variable to store all magazines
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self): #returns magazines name
            return self._name
        
    @name.setter
    def name(self, value): #sets magazines name
            if isinstance(value, str) and 2 <= len(value) <= 16:
             self._name = value

    @property
    def category(self): #returns magazines category
            return self._category
        
    @category.setter
    def category(self, value): #sets magazines category
            if isinstance(value, str) and 2 <= len(value) <= 16:
             self._category = value

    def articles(self):  # returns a list of articles published in the magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):   # returns a list of unique authors who have contributed to the magazine
        return list(set(article.author for article in self.articles()))

    def article_titles(self):  # returns a list of titles of articles published in the magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):    # returns a dictionary of authors who have contributed more than 2 articles to the magazine
        authors_count = {}   # counts the number of articles each author has contributed
        for article in self.articles():
            authors_count[article.author] = authors_count.get(article.author, 0) + 1   # increments the count for each author after checking whether they have contributed to the magazine
        result=  {author: count for author, count in authors_count.items() if count > 2}    # filters authors who have contributed more than 2 articles
        return result if result else None
    
    @classmethod    # returns the magazine that has published the most articles
    def top_publisher(cls):
        if not cls.all_articles:  # checks if there are no articles published   
            return None
        
        magazine_count = {}    # counts the number of articles published by each magazine
        for article in cls.all_articles:  # iterates through all articles and counts the number of articles for each magazine
            magazine_count[article.magazine] = magazine_count.get(article.magazine, 0) + 1

        top_magazine = max(magazine_count, key=magazine_count.get)    # finds the magazine with the highest article count
        return top_magazine if magazine_count[top_magazine] > 2 else None   # returns the top magazine only if it has more than 2 articles