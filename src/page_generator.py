from src.blocktype import markdown_to_html_node
from src.extract_title import extract_title
from src.markdown_blocks_converter import markdown_to_blocks

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()
    
    content_html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    final_temp = tpl.replace("{{ Title }}", title)
    final_html = final_temp.replace("{{ Content }}", content_html)
    print(final_html)
    with open(dest_path, "a", encoding="utf-8") as f:
            f.write(final_html)


def generate_pages_recursive(content_dir, template_path, dest_dir):
     #Iteration
     #if folder :
        # create folder in dest_dir
        # call generate_page_recursive on sub directories
    #if file:
        #if md file:
            #generate_page(md_file_path, template_path, dest_html_page)
    pass