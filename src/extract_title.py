import re

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if re.match(r"^# ", line):
            return line[2:].strip()
    raise Exception("must have a h1 header")
