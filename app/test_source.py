import unittest
from models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that run before every Test case
        '''

        self.new_source = Source("abc", "abc news", "blablabla", "general")

    def test_init(self):
        '''
        test case to test if the source object is initialized
        '''

        self.assertEqual("abc", self.new_source.source_id)
        self.assertEqual("abc news", self.new_source.source_name)

if __name__ == '__main__':
    unittest.main()
