import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
        self.assertListEqual([2], unique([2]))

    def test_empty_list(self):
        self.assertEqual([], unique([]))

    def test_one_item_many_times(self):
        self.assertEqual([1], unique([1,1,1,1,1,1]))
        self.assertEqual(["So tired"], unique(["So tired", "So tired"]))

    def test_many_items_many_times(self):
        self.assertEqual([1,2,3], unique([1,1,2,2,2,3,3,3,3]))
        self.assertEqual(["Hello world"], unique(["Hello world", "Hello world"]))

    def test_not_a_list(self):
        with self.assertRaises(TypeError):
            unique("I love programming")
        with self.assertRaises(TypeError):
            unique(1,2,3)

if __name__ == "__main__":
    unittest.main('listutil_test')