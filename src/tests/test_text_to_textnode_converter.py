import unittest

from src.text_to_textnodes_converter import text_to_textnodes
from src.textnode import TextNode, TextType

class TestTextToTextNodeFct(unittest.TestCase):

    def test_every_markdown(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
                                                        TextNode("This is ", TextType.TEXT),
                                                        TextNode("text", TextType.BOLD),
                                                        TextNode(" with an ", TextType.TEXT),
                                                        TextNode("italic", TextType.ITALIC),
                                                        TextNode(" word and a ", TextType.TEXT),
                                                        TextNode("code block", TextType.CODE),
                                                        TextNode(" and an ", TextType.TEXT),
                                                        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                                        TextNode(" and a ", TextType.TEXT),
                                                        TextNode("link", TextType.LINK, "https://boot.dev"),
                                                    ]
                            )
        
    def test_single_markdown(self):
        text = "This is some _italic_ but _italian_ text"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" but ", TextType.TEXT),
            TextNode("italian", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)])
    
    def test_two_different_markdown(self):
        url = "https://nsfw.com"
        text = f"**Bold text** into [link]({url})"
        self.assertEqual(text_to_textnodes(text),[
            TextNode("Bold text", TextType.BOLD),
            TextNode(" into ", TextType.TEXT),
            TextNode("link", TextType.LINK, url)
        ])