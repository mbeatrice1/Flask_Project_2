class Article:
    '''
    Article class  to define Article Objects
    '''

    def __init__(self, source_name, title, description, url_image, url, publication_time ):
        '''
        Article method that initialize attribute of an article class
        '''

        self.source_name = source_name
        self.article_title = title
        self.article_description = description
        self.article_image = url_image
        self.article_url = url
        self.publication_time = publication_time
        