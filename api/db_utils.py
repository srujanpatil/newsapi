import json
import mongoengine

from model import Article

# load config file
with open ('config.json', 'r') as f:
    config = json.load(f)

# connect to mongodb
connection_string = f'mongodb+srv://{config["Id"]}:{config["Password"]}@bi.itjnd.mongodb.net/{config["DB"]}?retryWrites=true&w=majority'
mongoengine.register_connection(alias='Test', db=config['DB'], host=connection_string)

# db-helper methods
def add_to_db(data:list) -> list:
    """
    Adds articles to DB
    
    Parameters:
        data (list): List of articles (dict)

    Returns:
        (list): A list of mongonengine article documents
    
    """
    try:
        return Article.objects().insert([Article(**dic) for dic in data], load_bulk=False)
    except Exception as e:
        return e

def list_articles(start:int) -> list:
    """
    Fetches the list of available articles
    
    Parameters:
        start (int): Start of page

    Returns:
        (list): A list of mongonengine article documents

    """
    try:
        if start:
            return Article.objects[start:start+config['Paginate']].all()
        else:
            return Article.objects[0:config['Paginate']].all()
    except:
        return []

def search_articles(query:str, start:int) -> list:
    """
    Fetches article by search keyword
    
    Parameters:
        query(str): A search keyword
        start (int): Start of page

    Returns:
        (list): A list of mongonengine article documents
    """
    try:
        if start:
            return Article.objects[start:start+config['Paginate']].search_text(query).order_by('$text_score')
        else:
            return Article.objects[0:config['Paginate']].search_text(query).order_by('$text_score')
    except:
        return []

def get_article_by_id(id:str) -> object:
    """
    Fetches article by id
    
    Parameters:
        id (str): 12-byte MongoDB ObjectID (12-byte BSON)

    Returns:
        (object): A mongonengine document (Article)
    """
    try:
        return Article.objects.get(id=id)
    except:
        return None

def get_count() -> int:
    """
    Fetches count of availble articles

    Returns:
        (int): A count of availble articles
    """
    try:
        return Article.objects.count()
    except:
        return None
