import unittest

from src.htmlnode import LeafNode
from src.textnode import TextType, TextNode, text_node_to_html_node

class TestConverter(unittest.TestCase):
    def test_invalid_text_type_raises(self):
        node = TextNode("some text", "bold") 
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_text(self):
        text = "some text"
        node = TextNode(text, TextType.TEXT)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.tag, None)
        self.assertEqual(leafnode.value, text)
    
    def test_bold(self):
        text = ""
        node = TextNode(text, TextType.BOLD)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.tag, "b")
        self.assertEqual(leafnode.value, text)
    
    def test_italic(self):
        text = "some italic text ?"
        node = TextNode(text, TextType.ITALIC)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.tag, "i")
        self.assertEqual(leafnode.value, text)
    
    def test_link(self):
        text = "click here"
        url = "www.whynot.com"
        node = TextNode(text, TextType.LINK, url)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.tag, "a")
        self.assertEqual(leafnode.value, text)
        self.assertEqual(leafnode.props, {"href": url})
    
    def test_image(self):
        text = "this is some image"
        url = "www.image_url.com"
        node = TextNode(text, TextType.IMAGE, url)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.tag, "img")
        self.assertEqual(leafnode.value, "")
        self.assertEqual(leafnode.props, {"src": url, "alt": text})

if __name__ == "__main__":
    unittest.main()