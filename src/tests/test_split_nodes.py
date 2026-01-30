import unittest
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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
    
    def test_non_text_nodes_unchanged(self):
        nodes = [TextNode("hello", TextType.BOLD)]
        self.assertEqual(split_nodes_image(nodes), nodes)

    def test_no_images_returns_original_text_node(self):
        node = TextNode("just plain text", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_single_image_middle(self):
        node = TextNode("hi ![cat](https://x.com/cat.png) bye", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("hi ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "https://x.com/cat.png"),
                TextNode(" bye", TextType.TEXT),
            ],
        )

    def test_two_images(self):
        node = TextNode(
            "A ![one](u1) B ![two](u2) C",
            TextType.TEXT,
        )
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("A ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "u1"),
                TextNode(" B ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "u2"),
                TextNode(" C", TextType.TEXT),
            ],
        )

    def test_image_at_start_and_end(self):
        node = TextNode("![a](u1) mid ![b](u2)", TextType.TEXT)
        self.assertEqual(
            split_nodes_image([node]),
            [
                TextNode("a", TextType.IMAGE, "u1"),
                TextNode(" mid ", TextType.TEXT),
                TextNode("b", TextType.IMAGE, "u2"),
            ],
        )


    def test_non_text_nodes_unchanged(self):
        nodes = [TextNode("hello", TextType.CODE)]
        self.assertEqual(split_nodes_link(nodes), nodes)

    def test_no_links_returns_original_text_node(self):
        node = TextNode("just plain text", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_single_link_middle(self):
        node = TextNode("hi [boot](https://boot.dev) bye", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("hi ", TextType.TEXT),
                TextNode("boot", TextType.LINK, "https://boot.dev"),
                TextNode(" bye", TextType.TEXT),
            ],
        )

    def test_two_links(self):
        node = TextNode("A [one](u1) B [two](u2) C", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("A ", TextType.TEXT),
                TextNode("one", TextType.LINK, "u1"),
                TextNode(" B ", TextType.TEXT),
                TextNode("two", TextType.LINK, "u2"),
                TextNode(" C", TextType.TEXT),
            ],
        )

    def test_link_at_start_and_end(self):
        node = TextNode("[a](u1) mid [b](u2)", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("a", TextType.LINK, "u1"),
                TextNode(" mid ", TextType.TEXT),
                TextNode("b", TextType.LINK, "u2"),
            ],
        )

    def test_link_split_does_not_touch_images(self):
        node = TextNode("x ![img](img-url) y [lnk](lnk-url) z", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode("x ![img](img-url) y ", TextType.TEXT),
                TextNode("lnk", TextType.LINK, "lnk-url"),
                TextNode(" z", TextType.TEXT),
            ],
        )

if __name__ == "__main__":
    unittest.main()