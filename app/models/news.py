class News:
    '''
    News class  to define Article Objects
    '''

    def __init__(self, source_name, title, description, url_image, url, publication_time ):
    '''
    News method that initialize attribute of an article class
    '''

        self.source_name = source_name
        self.news_title = title
        self.news_description = description
        self.news_image = url_image
        self.news_url = url
        self.publication_time = publication_time
        