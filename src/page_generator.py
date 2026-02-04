from src.blocktype import markdown_to_html_node
from src.extract_title import extract_title
from src.markdown_blocks_converter import markdown_to_blocks
import os

def generate_page(from_path, template_path, dest_path, basepath):
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()
    
    content_html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    final_temp = tpl.replace("{{ Title }}", title)
    final_html = final_temp.replace("{{ Content }}", content_html)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w", encoding="utf-8") as f:
            f.write(final_html)


def generate_pages_recursive(content_dir, template_path, dest_dir, basepath):
    os.makedirs(dest_dir, exist_ok=True)
    for entry in os.listdir(content_dir):
        src_path = os.path.join(content_dir, entry)

        if os.path.isdir(src_path):
            dest_path = os.path.join(dest_dir, entry)
            generate_pages_recursive(src_path, template_path, dest_path, basepath)
            continue

        if os.path.isfile(src_path) and entry.endswith(".md"):
            base_name = entry[:-3]
            dest_html = os.path.join(dest_dir, base_name+ ".html")
            generate_page(src_path, template_path, dest_html, basepath)
                