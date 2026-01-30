from src.textnode import TextType, TextNode
from src.markdown_links_extraction import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) %2 == 0:
                raise Exception("Unmatched delimiter")
            else:
                for index, part in enumerate(parts):
                    if part == "":
                        continue
                    if index%2 == 0:
                        new_node = TextNode(part, TextType.TEXT)
                    else:
                        new_node = TextNode(part, text_type)
                    new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(node)
            continue

        for alt, url in matches:
            markdown = f"![{alt}]({url})"
            parts = text.split(markdown, 1)
            before = parts[0]
            after = parts[1]
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            text = after
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes



            

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(node)
            continue

        for anchor, url in matches:
            markdown = f"[{anchor}]({url})"
            parts = text.split(markdown, 1)
            before = parts[0]
            after = parts[1]
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            text = after
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes