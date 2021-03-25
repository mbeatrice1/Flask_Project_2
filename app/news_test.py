import unittest
from models import news

News = news.News

class TestArticle(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Method that run before each test case
        '''
        self.new_news = News("abc", "covid", "blablablaa", "http", "http", "2020")

    def test_init(self):
        '''
        Test case that test if an article is initialized
        '''

        self.assertEqual("abc", self.new_news.source_name)
        self.assertEqual("covid", self.new_news.news_title)

if __name__=='__main__':
    unittest.main()