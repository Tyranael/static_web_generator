#! usr/bin/env bash

import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("Text", TextType.CODE, url="https:/google.com")
        node1 = TextNode("Text", TextType.CODE)
        self.assertNotEqual(node, node1)

    def test_eq_text_type(self):
        node = TextNode("Text", TextType.BOLD)
        node2 = TextNode("Text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_init_text_node(self):
        node = TextNode("text", TextType.BOLD)
        self.assertIsInstance(node, TextNode)


if __name__ == "__main__":
    unittest.main()