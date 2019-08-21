import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )

if __name__ == "__main__":
    unittest.main('listutil_test')