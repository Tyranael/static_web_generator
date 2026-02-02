from enum import Enum
import re
from src.htmlnode import ParentNode
from src.markdown_blocks_converter import markdown_to_blocks
from src.text_to_textnodes_converter import text_to_textnodes
from src.textnode import text_node_to_html_node, TextNode, TextType

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

def inline_to_leafnodes(text_nodes):
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def blocktype_to_html_node(block, blocktype):
    match blocktype:

        case BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block)
            children = inline_to_leafnodes(text_nodes)
            return ParentNode("p", children)
        
        case BlockType.HEADING:
            number = block.split()[0].count("#")
            parsed_block = block[number+1:]
            text_nodes = text_to_textnodes(parsed_block)
            children = inline_to_leafnodes(text_nodes)
            return ParentNode(f"h{number}", children)
        
        case BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = [line[1:] if line.startswith(">") else line for line in lines]
            parsed_block = " ".join(line.lstrip() for line in new_lines)
            text_nodes = text_to_textnodes(parsed_block)
            children = inline_to_leafnodes(text_nodes)
            return ParentNode("blockquote", children)
        
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            new_lines = [line[2:] for line in lines if line.startswith("- ")]
            li_nodes = []
            for item in new_lines:
                text_nodes = text_to_textnodes(item)
                children = inline_to_leafnodes(text_nodes)
                li_nodes.append(ParentNode("li", children))
            return ParentNode("ul", li_nodes)

        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                index = line.index(".")
                new_lines.append(line[index+2:])
            li_nodes = []
            for item in new_lines:
                text_nodes = text_to_textnodes(item)
                children = inline_to_leafnodes(text_nodes)
                li_nodes.append(ParentNode("li", children))
            return ParentNode("ol", li_nodes)
        case BlockType.CODE:
            lines = block.split("\n")

        
            code_text = "\n".join(lines[1:-1])

            code_leaf = text_node_to_html_node(TextNode(code_text, TextType.CODE))
            return ParentNode("pre", [code_leaf])
        case _:
            raise Exception("must be valid BlockType")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        node = blocktype_to_html_node(block, block_type)
        children.append(node)
    return ParentNode("div", children)