import unittest
from src.blocktype import markdown_to_html_node

class TestMarkdownsToParentNodes(unittest.TestCase):
    def test_paragraph_block(self):
        text = "This is a paragraph text, with a **bolded** word"
        self.assertEqual(markdown_to_html_node(text).to_html(), "<div><p>This is a paragraph text, with a <b>bolded</b> word</p></div>")
    
    def test_heading_block(self):
        text = "#### Heading 4 right ?"
        self.assertEqual(markdown_to_html_node(text).to_html(), "<div><h4>Heading 4 right ?</h4></div>")
    
    def test_quote_block(self):
        text = """
>This is some quoted text
>with some newlines
>for testing purposes
"""
        self.assertEqual(markdown_to_html_node(text).to_html(), "<div><blockquote>This is some quoted text with some newlines for testing purposes</blockquote></div>")

    def test_ul_list(self):
        text = """
- Item one
- Item **two**
- Item _three_
"""
        self.assertEqual(markdown_to_html_node(text).to_html(), "<div><ul><li>Item one</li><li>Item <b>two</b></li><li>Item <i>three</i></li></ul></div>")
    
    def test_ol_list(self):
        text ="""
1. Item one
2. Item two
3. Item three
"""
        self.assertEqual(markdown_to_html_node(text).to_html(), "<div><ol><li>Item one</li><li>Item two</li><li>Item three</li></ol></div>")
    
    def test_code_block(self):
        text = """```py
print("hi")
print("yo")
```"""
        self.assertEqual(markdown_to_html_node(text).to_html(),'<div><pre><code>print("hi")\nprint("yo")</code></pre></div>')
