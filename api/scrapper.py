import json
import datetime
import logging
import logging.handlers
import requests
from bs4 import BeautifulSoup

from db_utils import add_to_db

# load config file
with open ('config.json', 'r') as f:
    config = json.load(f)

# setup logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

if config['DEBUG'] == 'True':
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
else:
    logger.setLevel(logging.INFO)
    file_handler = logging.handlers.TimedRotatingFileHandler('logs/scrapper.log', when='midnight', interval=1)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def fetch_articles(url:str) -> list:
    """
    Fetches Articles from RSS links
    
    Parameters:
        url (str): theguardian.com rss link

    Returns:
        (list): A list of news articles

    """
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'xml')
    except Exception as e:
        logger.exception(e)
        return []

    articles = []
    for item in soup.find_all('item'):
        articles.append({
            "Link": item.find('link').text,
            "Title": item.find('title').text,
            "PubDate": datetime.datetime.strptime(item.find('dc:date').text,'%Y-%m-%dT%H:%M:%S%z'),
            "Author": item.find('dc:creator').text,
            "Description": '. '.join([p.text for p in  BeautifulSoup(item.find('description').text, 'html.parser').find_all('p')]),
            "Category": [cat.text for cat in item.find_all('category')]
        })
    return articles

def fetch_rss(config:dict) -> list:
    """
    Fetches Articles from RSS links
    
    Parameters:
        config (dict): dictionary of config.js

    Returns:
        (list): A list of news articles
        
    """
    data = []
    for rss in config['rss']:
            data.extend(fetch_articles(url=rss))
            logger.debug(f'Fetch of {rss} completed')
    return data

if __name__ == '__main__':
    logger.info('Scrapper Started')
    try:
        logger.info('Fetching articles')
        articles = fetch_rss(config)
        logger.info('Adding to database')
        add_to_db(articles)
        logger.info('Completed')
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info('Scrapper Stopped')
