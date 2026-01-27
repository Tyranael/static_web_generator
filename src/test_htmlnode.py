#! usr/bin/env bash

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none_returns_empty_str(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_empty_dict_returns_empty_str(self):
        node = HTMLNode(props={})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_one_entry_dict(self):
        node = HTMLNode(props={"p": "some text here"})
        expected = ' p="some text here"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_two_entries_dict(self):
        node = HTMLNode(props={"p": "some text here", "h1": "some big header"})
        expected = ' p="some text here" h1="some big header"'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()