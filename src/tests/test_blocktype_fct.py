import unittest
from src.blocktype import BlockType, block_to_blocktype



class TestBlockToBlockType(unittest.TestCase):
    # -------- Heading --------
    def test_heading_level_1(self):
        block = "# Hello"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_heading_level_6(self):
        block = "###### Hello"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_heading_not_if_hash_not_at_start(self):
        block = "Hello # world"
        self.assertNotEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_heading_not_if_7_hashes(self):
        block = "####### Too many"
        self.assertNotEqual(block_to_blocktype(block), BlockType.HEADING)

    # -------- Code --------
    def test_code_block_basic(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    def test_code_block_wins_over_heading_like_content(self):
        block = "```\n# not a heading\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    def test_code_block_requires_closing_backticks(self):
        block = "```\nprint('hi')\n"
        self.assertNotEqual(block_to_blocktype(block), BlockType.CODE)

    # -------- Quote --------
    def test_quote_single_line_no_space(self):
        block = ">quote sans espace"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_quote_multi_line_mixed_spaces(self):
        block = "> quote avec espace\n>deuxième ligne\n> troisième"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_quote_fails_if_one_line_missing_greater_than(self):
        block = "> ok\npas ok"
        self.assertNotEqual(block_to_blocktype(block), BlockType.QUOTE)

    # -------- Unordered list --------
    def test_unordered_list_dash(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_fails_if_missing_space_after_dash(self):
        block = "-item 1\n-item 2"
        self.assertNotEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_fails_if_mixed_prefixes(self):
        block = "- item 1\n* item 2\n- item 3"
        self.assertNotEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    # -------- Ordered list --------
    def test_ordered_list_valid_increment(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    def test_ordered_list_fails_if_not_incrementing(self):
        block = "1. one\n3. two\n4. three"
        self.assertNotEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    def test_ordered_list_fails_if_missing_space_after_dot(self):
        block = "1.one\n2. two"
        self.assertNotEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    def test_ordered_list_fails_if_zero_padded(self):
        block = "01. one\n2. two"
        self.assertNotEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    # -------- Paragraph fallback --------
    def test_paragraph_default(self):
        block = "Juste un paragraphe."
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "Deux lignes\nmême paragraphe"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
