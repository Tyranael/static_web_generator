import os
import shutil
from src.page_generator import generate_pages_recursive
import sys

def copy_static(src, dest):
        if not os.path.exists(src):
            raise Exception("must put valid source directory")
        if os.path.exists(dest):
            shutil.rmtree(dest)
        os.mkdir(dest)

        for entry in os.listdir(src):
            src_path = os.path.join(src, entry)
            dest_path = os.path.join(dest, entry)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
            else:
                copy_static(src_path, dest_path)



def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.endswith("/"):
        basepath += "/"
    
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public", basepath)
    print("basepath =", basepath)



main()