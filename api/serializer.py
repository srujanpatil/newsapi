from db_utils import get_article_by_id, list_articles, search_articles

class ArticleSerializer:

    @staticmethod
    def get_list(start:int) -> dict:
        """
        Serializes list of articles
        
        Parameters:
            start (int): Start of page

        Returns:
            (dict): A dictionary of list of articles

        """
        articles = list_articles(start)
        if articles:
            return {
                "Articles": [{"Link": article.Link, "Title": article.Title, "Date": article.PubDate.strftime("%m/%d/%Y %H:%M:%S"), "Article": f"/article/{article.id}"} for article in articles()]
            }
        else:
            return {
                "Message": "No Articles Found"
            }

    @staticmethod
    def get_search(query:str, start:int) -> dict:
        """
        Serializes list of queried articles

        Parameters: 
            query(str): A search keyword
            start(int): Start of page
        
        Returns:
            (dict): A dictionary of list of articles

        """
        articles = search_articles(query, start)
        if articles:
            return {
                "Articles": [{"Link": article.Link, "Title": article.Title, "Date": article.PubDate.strftime("%m/%d/%Y %H:%M:%S"), "Article": f"/article/{article.id}"} for article in articles()]
            }
        else:
            return {
                "Message": "No Articles Found"
            }

    @staticmethod
    def get_article(id:str) -> dict:
        """
        Serializes an article document
        
        Parameters:
            id (str): 12-byte MongoDB ObjectID (12-byte BSON)

        Returns:
            (dict): Article dictionary

        """
        article = get_article_by_id(id)
        if article:
            return {
                "Link": article.Link, 
                "Title": article.Title, 
                "Date": article.PubDate.strftime("%m/%d/%Y %H:%M:%S"),
                "Author": article.Author,
                "Category": article.Category
            }
        else:
            return {
                "Message": "Article Not Found or Invalid Input"
            }
