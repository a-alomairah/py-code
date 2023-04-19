import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def organize_files(directory):
    # Create subdirectories if they don't exist
    Path(directory, "Documents").mkdir(exist_ok=True)
    Path(directory, "Videos").mkdir(exist_ok=True)
    Path(directory, "Pictures").mkdir(exist_ok=True)
    Path(directory, "Other").mkdir(exist_ok=True)

    for file in os.listdir(directory):
        if file == "Documents":
            continue
        elif file == "Videos":
            continue
        elif file == "Pictures":
            continue
        elif file == "Other":
            continue

        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path):
            organize_files(file_path)
        else:
            file_extension = file.split(".")[-1].lower()
            if file_extension in ["doc", "docx", "pdf", "txt"]:
                shutil.move(file_path, os.path.join(directory, "Documents"))
            elif file_extension in ["mp4", "mov", "avi", "mkv"]:
                shutil.move(file_path, os.path.join(directory, "Videos"))
            elif file_extension in ["jpg", "jpeg", "png", "gif"]:
                shutil.move(file_path, os.path.join(directory, "Pictures"))
            else:
                shutil.move(file_path, os.path.join(directory, "Other"))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select a directory to organize")
    if not directory:
        print("No directory selected.")
        exit()

    organize_files(directory)
    print("Done organizing.")
