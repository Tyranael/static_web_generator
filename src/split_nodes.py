from src.textnode import TextType, TextNode

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