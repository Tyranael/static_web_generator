import unittest

from src.markdown_links_extraction import extract_markdown_links, extract_markdown_images

class TestExtractors(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images("This is some text without anything")
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a link to my domain [Shaun's domain](https://shaun.com)")
        self.assertListEqual([("Shaun's domain", "https://shaun.com")], matches)
