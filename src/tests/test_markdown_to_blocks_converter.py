import unittest

from src.markdown_blocks_converter import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_several_paragraphs_with_single_newlines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        self.assertEqual(markdown_to_blocks(md),  [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],)


    def test_single_line_str(self):
        md = "This is some classical text"
        self.assertEqual(markdown_to_blocks(md), ["This is some classical text"])


    def test_one_paragraph_several_newlines(self):
        md = """
This is some text.
Going onto another line.
Without going into a new paragraph though.
Anyway, bye !
"""
        self.assertEqual(markdown_to_blocks(md), [
            "This is some text.\nGoing onto another line.\nWithout going into a new paragraph though.\nAnyway, bye !",

        ])