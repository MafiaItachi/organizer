import os
import shutil

# Define the directory where the files are located
parent_directory = "C:/VICTUS/ENTERTANMENT"

def move_files_and_delete_subfolders():
    # Loop through all subfolders in the parent directory
    for subdir, dirs, files in os.walk(parent_directory, topdown=False):
        # Skip the parent directory itself
        if subdir == parent_directory:
            continue
        
        # Move all files from the subfolder to the parent directory
        for file_name in files:
            file_path = os.path.join(subdir, file_name)
            destination = os.path.join(parent_directory, file_name)

            # Move file to the parent directory if it's not already there
            if not os.path.exists(destination):
                shutil.move(file_path, destination)
                print(f'Moved {file_name} to {parent_directory}')
            else:
                print(f'{file_name} already exists in the parent directory')

        # Remove the now-empty subfolder
        if not os.listdir(subdir):  # Check if the subfolder is empty
            os.rmdir(subdir)
            print(f'Deleted empty folder: {subdir}')

if __name__ == '__main__':
    move_files_and_delete_subfolders()
