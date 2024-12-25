import os
import shutil
import re

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
            cleaned_name = file_name[:resolution_pattern.end()] + os.path.splitext(file_name)[1]
        else:
            # Return the original name if no patterns match
            cleaned_name = file_name

    # Replace dots with spaces (except for the extension) and convert to uppercase
    name, extension = os.path.splitext(cleaned_name)
    cleaned_name = name.replace('.', ' ').upper() + extension.lower()

    return cleaned_name

def move_files():
    # Loop through all the files in the directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)

        # Ignore directories, process only files with allowed extensions
        if os.path.isfile(file_path) and any(file_name.endswith(ext) for ext in allowed_extensions):
            # Clean the file name
            cleaned_name = clean_file_name(file_name)

            # Handle TV shows with season/episode patterns
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

            # Remove year from TV show folders if present
            folder_name = re.sub(r'\s\d{4}$', '', folder_name)

            # Create a folder based on the extracted name
            folder_path = os.path.join(source_directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Rename the file with the cleaned name
            new_file_path = os.path.join(source_directory, cleaned_name)
            os.rename(file_path, new_file_path)

            # Move the renamed file to the correct folder
            dest_path = os.path.join(folder_path, cleaned_name)
            if not os.path.exists(dest_path):
                shutil.move(new_file_path, dest_path)
                print(f"Moved {cleaned_name} to {folder_path}")
            else:
                print(f"{cleaned_name} is already in the correct folder")

if __name__ == '__main__':
    move_files()
