import os
import shutil
import re
from collections import defaultdict

# Define the directory where the files are located
source_directory = "C:/VICTUS/ENTERTANMENT"

# Specify allowed file types (e.g., only move media files)
allowed_extensions = ['.mkv', '.mp4', '.avi']

def clean_file_name(file_name):
    # Check for SxxExx pattern and truncate after it
    tv_pattern = re.search(r'(S\d{2}E\d{2})', file_name, re.IGNORECASE)
    if tv_pattern:
        cleaned_name = file_name[:tv_pattern.end()] + os.path.splitext(file_name)[1]
    else:
        # Otherwise, truncate after "1080p"
        resolution_pattern = re.search(r'1080p', file_name, re.IGNORECASE)
        if resolution_pattern:
            cleaned_name = file_name[:resolution_pattern.start()] + os.path.splitext(file_name)[1]
        else:
            # Return the original name if no patterns match
            cleaned_name = file_name

    # Replace dots with spaces (except for the extension) and convert to uppercase
    name, extension = os.path.splitext(cleaned_name)
    cleaned_name = name.replace('.', ' ').upper() + extension.lower()

    return cleaned_name

def prioritize_folder(folder_name, existing_folders):
    # Check for folders with the same base name but with a year
    base_folder_name = re.sub(r'\s\d{4}$', '', folder_name)
    for existing_folder in existing_folders:
        if existing_folder.startswith(base_folder_name) and re.search(r'\d{4}', existing_folder):
            return existing_folder
    return folder_name

def move_files():
    folder_files_map = defaultdict(list)

    # Collect all existing folders in the source directory
    existing_folders = [name.upper() for name in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, name))]

    # Traverse through all files and subdirectories
    for root, dirs, files in os.walk(source_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Ignore files that don't have allowed extensions
            if any(file_name.endswith(ext) for ext in allowed_extensions):
                # Clean the file name
                cleaned_name = clean_file_name(file_name)

                # Rename the file with the cleaned name if needed
                new_file_path = os.path.join(root, cleaned_name)
                if file_path != new_file_path:
                    os.rename(file_path, new_file_path)
                    file_path = new_file_path

                # Determine the folder for organizing the file
                tv_match = re.match(r'([a-zA-Z0-9\ \-]+)[Ss]\d{2}[Ee]\d{2}', cleaned_name, re.IGNORECASE)
                if tv_match:
                    # Extract and clean show name
                    show_name = tv_match.group(1).strip()
                    folder_name = show_name.upper()
                else:
                    # Handle movies with year patterns
                    movie_match = re.match(r'([a-zA-Z0-9\ \-]+)\ (\d{4})', cleaned_name)
                    if movie_match:
                        # Extract and clean movie name
                        movie_name = movie_match.group(1).strip()
                        year = movie_match.group(2)
                        folder_name = f"{movie_name} {year}".upper()
                    else:
                        # Default case: Skip files that don't match known patterns
                        print(f"Skipping file: {file_name} (no matching pattern)")
                        continue

                # Prioritize folders with years if a similar folder exists
                folder_name = prioritize_folder(folder_name, existing_folders)

                # Replace dots globally with spaces in the folder name
                folder_name = re.sub(r'\.', ' ', folder_name)

                # Remove all occurrences of "1080" or "1080P" in the folder name
                folder_name = re.sub(r'\s?1080[pP]?', '', folder_name)

                # Create the destination folder
                folder_path = os.path.join(source_directory, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    existing_folders.append(folder_name)

                # Move the file to the destination folder
                dest_path = os.path.join(folder_path, cleaned_name)
                if not os.path.exists(dest_path):
                    shutil.move(file_path, dest_path)

                # Add the file name to the folder's list
                folder_files_map[folder_name].append(cleaned_name)

    if not folder_files_map:
        print("✨==============================✨")
        print(" All files are already organized!")
        print("✨==============================✨")
    else:
        # Print the organized folders and their contents
        for folder_name, file_list in folder_files_map.items():
            print("\n✨==============================✨")
            print(f" 📂 Folder Created : {folder_name}")
            for file_name in file_list:
                print(f" ↪️📁 Edited Movie Name: {file_name}")
            print("✨==============================✨\n")

if __name__ == '__main__':
    move_files()

# Written by [Your Name]
