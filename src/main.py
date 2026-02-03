import os
import shutil


def copy_static(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    # 2) walk source
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dest_path = os.path.join(dest, entry)

        if os.path.isfile(src_path):
            print(f"Copying {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            # directory
            copy_static(src_path, dest_path)


copy_static("static", "public")