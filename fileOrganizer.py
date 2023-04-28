import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def organize_files(directory):
    # Create subdirectories if they don't exist
    dir_names = ["Documents", "Videos", "Pictures", "Other"]
    for dir_name in dir_names:
        Path(directory, dir_name).mkdir(exist_ok=True)

    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)) and file in dir_names:
            continue

        file_path = os.path.join(directory, file)

        # only do operations on files and not directories.
        if os.path.isfile(file_path):
            file_extension = file.split(".")[-1].lower()
            if file_extension in ["doc", "docx", "pdf", "txt","odf","odt","csv"]:
                dest_dir = os.path.join(directory, "Documents")
            elif file_extension in ["mp4", "mov", "avi", "mkv","webm"]:
                dest_dir = os.path.join(directory, "Videos")
            elif file_extension in ["jpg", "jpeg", "png", "gif"]:
                dest_dir = os.path.join(directory, "Pictures")
            else:
                dest_dir = os.path.join(directory, "Other")
            
            # Check if a file with the same name exists in the destination folder
            dest_file_path = os.path.join(dest_dir, file)
            if os.path.exists(dest_file_path):
                # If the modification time of the source file is the same or earlier than the
                # modification time of the destination file, overwrite the destination file
                if os.stat(file_path).st_mtime <= os.stat(dest_file_path).st_mtime:
                    os.remove(file_path)
                    continue
            # If the source file is newer than the destination file, move it to the destination folder
            shutil.move(file_path, dest_dir)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select a directory to organize")
    if not directory:
        print("No directory selected.")
        exit()

    organize_files(directory)
    print("Done organizing.")
