import re

def extract_title(markdown):
    if not re.match(r"^#{1} ", markdown):
        raise Exception("must be a h1 header")
    return markdown[2:]