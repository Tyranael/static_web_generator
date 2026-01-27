import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_child_without_tag(self):
        child_node = LeafNode(tag=None, value="some cool text here")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div>some cool text here</div>")
    
    def test_to_html_with_parent_node_as_child(self):
        child_node = LeafNode("b", "bold text", props = {"href": "www.link.com"})
        parent_node = ParentNode("div", [child_node])
        grand_parent_node = ParentNode("h1", [parent_node])
        self.assertEqual(grand_parent_node.to_html(), '<h1><div><b href="www.link.com">bold text</b></div></h1>')
    
    def test_to_html_with_two_children(self):
        child_node_1 = LeafNode("p", "child_one")
        child_node_2 = LeafNode("i", "child_two")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), "<div><p>child_one</p><i>child_two</i></div>")