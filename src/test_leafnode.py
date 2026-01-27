import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_constructor(self):
        leafnode = LeafNode("p", "some cool text")
        self.assertIsInstance(leafnode, LeafNode)

    def test_leafnode_testing_valueerror(self):
        leafnode = LeafNode("a", None, {"href": "https:/bootdev.com"})
        with self.assertRaises(ValueError):
            leafnode.to_html()
    
    def test_leafnode_to_html_no_props_case(self):
        leafnode = LeafNode("h1", "big ass header")
        self.assertEqual(leafnode.to_html(), "<h1>big ass header</h1>")
    
    def test_leafnode_to_html_props_case(self):
        leafnode = LeafNode("a", "cliquez!!", {"href": "www.morsay.com"})
        self.assertEqual(leafnode.to_html(), '<a href="www.morsay.com">cliquez!!</a>')
    
    def test_leafnode_raw_text_return(self):
        leafnode = LeafNode(tag=None, value="J'en veux Djo")
        self.assertEqual(leafnode.to_html(), "J'en veux Djo")

if __name__ == "__main__":
    unittest.main()