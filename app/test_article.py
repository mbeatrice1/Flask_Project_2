from app import app
from .models import source
from .models import article
import urllib.request, json

Source = source.Source
Article = article.Article

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the base urls
source_base_url = app.config['NEWS_API_SOURCE_URL']
article_base_url = app.config['NEWS_API_ARTICLE_URL']

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

def get_articles_from_source(source_id):
    '''
    Function that get articles from a given sources
    '''

    get_article_url = article_base_url.format(source_id, api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            get_article_list = get_article_response['articles']
            article_results = process_article_results(get_article_list)
        
    return article_results


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

def process_article_results(article_list):
    '''
    Function that process list of articles got from api an transform them
    '''

    article_results = []

    for item in article_list:
        source_name = item['source'].get('name')
        article_title = item.get('title')
        article_description = item.get('description')
        article_image = item.get('urlToImage')
        article_url = item.get('url')
        article_publication_time = item.get('publishedAt')

        article_data = Article(source_name, article_title, article_description, article_image, article_url, article_publication_time)
        article_results.append(article_data)

    return article_results


