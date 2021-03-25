from flask import render_template
from app import app
from .request import get_sources
from .request import get_articles_from_source

@app.route("/")
def index():
    '''
    View root function that returns index and page and its data
    '''

    # Getting sport sources
    sport_sources = get_sources('sports')

    # Getting business sources
    business_sources = get_sources('business')

    # Getting entertainment sources
    # entertainment_sources = get_sources('entertainment')

    # Getting general sources
    general_sources = get_sources('general')

    # Getting health sources
    health_sources = get_sources('health')

    # Getting science sources
    science_sources = get_sources('science')

    # Getting technology sources
    technology_sources = get_sources('technology')


    title = "Home - News Article"

    return render_template("index.html", title = title, sports = sport_sources, general = general_sources, technology = technology_sources, health = health_sources, science = science_sources, business = business_sources)

@app.route("/article/<source_id>")
def source(source_id):
    '''
    View route function that returns source page showing all articles of a given source
    '''

    title = f'{source_id}'
    articles_list = get_articles_from_source(source_id)

    return render_template('source.html',title = title, articles = articles_list)
    