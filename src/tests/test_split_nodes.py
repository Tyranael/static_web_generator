import unittest
from src.split_nodes import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodesFct(unittest.TestCase):

    def test_single_node_case_no_text(self):
        txt = "This some text for the test"
        node = TextNode(txt, TextType.BOLD)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [TextNode(txt, TextType.BOLD)])
    
    def test_single_node_code(self):
        txt = "a`b`c"
        node = TextNode(txt, TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [TextNode("a", TextType.TEXT), TextNode("b", TextType.CODE), TextNode("c", TextType.TEXT)])
    
    def test_with_several_nodes(self):
        txt_1 = "hi there"
        txt_2 = "hello **world** !"

        node_1 = TextNode(txt_1, TextType.TEXT)
        node_2 = TextNode(txt_2, TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node_1, node_2], "**", TextType.BOLD), 
                         [
                             TextNode(txt_1, TextType.TEXT), 
                             TextNode("hello ", TextType.TEXT),
                             TextNode("world", TextType.BOLD),
                             TextNode(" !", TextType.TEXT)])
        
    def test_unmatched_delimiter(self):
        txt = "Yoo **man** ! How are **you doing ?"
        node = TextNode(txt, TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)