from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType

def text_to_textnodes(text):
    output = []
    actual_node = [TextNode(text, TextType.TEXT)]
    delimiters = {"`": TextType.CODE,
                  "**": TextType.BOLD,
                  "_": TextType.ITALIC,
                  
                 }
    for k, v in delimiters.items():
        new_nodes = split_nodes_delimiter(actual_node, k, v)
        output.append(new_nodes)
        actual_node = new_nodes
    actual_node = output[-1]
    actual_node = split_nodes_image(actual_node)
    actual_node = split_nodes_link(actual_node)
    return actual_node
