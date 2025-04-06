from pathlib import Path
import shutil, os



def delete_all_public_files():
    directory = Path("public/")

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)

def copy_all_files():
    # copy_directory('src/', 'public/')
    copy_directory('src/static/', 'public/')
    
def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest,item)
        print(f'Copying: {src_path} to: {dest_path}')

        if os.path.isdir(src_path):
            copy_directory(src_path, dest_path)
        else:
            #copy file
            shutil.copy2(src_path, dest_path)