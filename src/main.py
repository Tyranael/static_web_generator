import os
import shutil
from src.page_generator import generate_pages_recursive

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
                print(f"Copying {src_path} -> {dest_path}")
                shutil.copy(src_path, dest_path)
            else:
                copy_static(src_path, dest_path)



def main():
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()