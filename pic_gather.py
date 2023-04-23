import os
import shutil

# Get the path of the root folder containing the subfolders with the pictures from user input
root_folder = input("Enter the path of the root folder: ")

# Define the name of the output folder (as a subfolder in the root folder)
output_folder_name = "all_pictures"
output_folder_path = os.path.join(root_folder, output_folder_name)

# Create the output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

# Define a list of image file extensions
image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

# Loop through all subfolders in the root folder
for subdir, dirs, files in os.walk(root_folder):
    # Get the name of the current subfolder
    folder_name = os.path.basename(subdir)
    # Loop through all files in the current subfolder
    for i, file in enumerate(files):
        # Check if the file is an image file
        _, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            # Define the full path of the current picture
            picture_path = os.path.join(subdir, file)
            # Define the new name for the picture (with the folder name and a number)
            new_name = "{}_{}_{}".format(folder_name, i+1, file)
            # Define the full path of the new picture in the output folder
            new_path = os.path.join(output_folder_path, new_name)
            # Copy the current picture to the output folder with the new name
            shutil.copy(picture_path, new_path)
