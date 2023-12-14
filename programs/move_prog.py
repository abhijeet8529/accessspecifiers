import shutil
import os

source_folder = "C:\\Users\\DELL\\Desktop\\studio\\New folder"
dest_folder = "C:\\Users\\DELL\\Desktop\\studio\\Python_basics\\methods"

if os.path.exists(source_folder) and os.path.isdir(dest_folder):
    files = os.listdir(source_folder)
    
    for file in files:
        source_file = os.path.join(source_folder, file)
        dest_file = os.path.join(dest_folder, file)
        
        shutil.move(source_file, dest_file)