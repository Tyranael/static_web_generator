from enum import Enum
#from src.markdown_blocks_converter import markdown_to_blocks
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(md_block):
    if re.match(r"^#{1,6} ", md_block):
        return BlockType.HEADING
    if md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    lines = md_block.split("\n")
    if all(line.startswith(">") for line in lines if line != ""):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines if line != ""):
        return BlockType.UNORDERED_LIST
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines) if line != ""):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH