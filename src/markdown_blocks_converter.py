def markdown_to_blocks(markdown):
    separated_blocks = markdown.split("\n\n")
    return [block.strip() for block in separated_blocks]