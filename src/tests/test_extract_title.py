import unittest
from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_h1_header(self):
        title = "# This is a valid h1 header"
        self.assertEqual(extract_title(title), "This is a valid h1 header")
    
    def test_h2_header(self):
        title = "## This is a valid h2 header"
        with self.assertRaises(Exception):
            extract_title(title)
    
    def test_h1_header_with_tag_in_the_middle(self):
        title = "# This is a valid h1 h##eader"
        self.assertEqual(extract_title(title), "This is a valid h1 h##eader")
    
    def test_no_tag(self):
        title = "This is not a valid header"
        with self.assertRaises(Exception):
            extract_title(title)