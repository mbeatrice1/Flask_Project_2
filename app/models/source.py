class Source:
    '''
    Source class  to define Source Objects
    '''

    def __init__(self, id, name, description, category):
        '''
        Source method that initialize attribute of a source class
        '''
        self.source_id = id
        self.source_name = name
        self.source_description = description
        self.category = category