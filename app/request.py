from app import app
from .models import source
from .models import news
import urllib.request, json

Source = source.Source
News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the base urls
source_base_url = app.config['NEWS_API_SOURCE_URL']
news_base_url = app.config['NEWS_API_NEWS_URL']

def get_sources(category):
    '''
    Function that get the sources data from the api
    '''

    get_sources_url = source_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            get_sources_list = get_sources_response['sources']
            sources_results = process_results(get_sources_list)

    return sources_results

def get_news_from_source(source_id):
    '''
    Function that get articles from a given sources
    '''

    get_news_url = news_base_url.format(source_id, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['newss']:
            get_news_list = get_news_response['newss']
            news_results = process_news_results(get_news_list)
        
    return news_results


def process_results(source_list):
    '''
    Function that processes the sources data to transform them to a list of objects

    Args:
        source_list: list of dictionaries that hold news data
    Returns:
        source_results: A list of source object
    '''

    source_results = []

    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        category = item.get('category')

        source_data = Source(id, name, description, category)
        source_results.append(source_data)

    return source_results

def process_news_results(news_list):
    '''
    Function that process list of articles got from api an transform them
    '''

    news_results = []

    for item in news_list:
        source_name = item['source'].get('name')
        news_title = item.get('title')
        news_description = item.get('description')
        news_image = item.get('urlToImage')
        news_url = item.get('url')
        news_publication_time = item.get('publishedAt')

        news_data = Article(source_name, article_title, article_description, article_image, article_url, article_publication_time)
        news_results.append(article_data)

    return news_results


