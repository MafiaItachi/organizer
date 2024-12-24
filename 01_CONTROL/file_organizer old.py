import os
import shutil
import re

# Define the directory where the files are located
source_directory = "C:/VICTUS/ENTERTANMENT"

# Specify allowed file types (e.g., only move media files)
allowed_extensions = ['.mkv', '.mp4', '.avi']

def move_files():
    # Loop through all the files in the directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)
        
        # Ignore directories, process only files with allowed extensions
        if os.path.isfile(file_path) and any(file_name.endswith(ext) for ext in allowed_extensions):
            # Use regex to extract the full show name before season/episode info
            match = re.match(r'([a-zA-Z0-9\s\.\-]+)[Ss]\d{2}E\d{2}', file_name)
            if match:
                # Get the show name, clean up dots, and strip trailing spaces
                show_name = match.group(1).replace('.', ' ').strip()
                
                # Create a folder based on the show name
                folder_path = os.path.join(source_directory, show_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Move the file to the correct folder
                dest_path = os.path.join(folder_path, file_name)
                
                # Only move if the file is not already in the correct folder
                if not os.path.exists(dest_path):
                    shutil.move(file_path, dest_path)
                    print(f'Moved {file_name} to {folder_path}')
                else:
                    print(f'{file_name} is already in the correct folder')

            else:
                # In case the regex doesn't match (e.g., the show name has no season/episode pattern)
                # Check if the file belongs to a known show (e.g., "What If")
                if 'what.if' in file_name.lower():
                    show_name = 'What If'
                    folder_path = os.path.join(source_directory, show_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    dest_path = os.path.join(folder_path, file_name)

                    # Move the file to the correct folder
                    if not os.path.exists(dest_path):
                        shutil.move(file_path, dest_path)
                        print(f'Moved {file_name} to {folder_path}')
                    else:
                        print(f'{file_name} is already in the correct folder')

if __name__ == '__main__':
    move_files()














import os
import shutil
import re

# Define the directory where the files are located
source_directory = "C:/VICTUS/ENTERTANMENT"

# Specify allowed file types (e.g., only move media files)
allowed_extensions = ['.mkv', '.mp4', '.avi']

def move_files():
    # Loop through all the files in the directory
    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)
        
        # Ignore directories, process only files with allowed extensions
        if os.path.isfile(file_path) and any(file_name.endswith(ext) for ext in allowed_extensions):
            # Use regex to capture the show name before the season/episode pattern
            match = re.match(r'([a-zA-Z0-9\s\.\-]+?)(?=[Ss]\d{2}E\d{2})', file_name)
            
            if match:
                # Get the show name, clean up dots and strip trailing spaces
                show_name = match.group(1).replace('.', ' ').strip()
                
                # Capitalize the show name
                show_name = ' '.join([word.capitalize() for word in show_name.split()])
                
                # Create a folder based on the show name
                folder_path = os.path.join(source_directory, show_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Move the file to the correct folder
                dest_path = os.path.join(folder_path, file_name)
                
                # Only move if the file is not already in the correct folder
                if not os.path.exists(dest_path):
                    shutil.move(file_path, dest_path)
                    print(f'Moved {file_name} to {folder_path}')
                else:
                    print(f'{file_name} is already in the correct folder')
            else:
                # If regex doesn't match, it means the file does not contain season/episode info
                # This condition should not be triggered with correct file names
                print(f'No valid match for {file_name}')

if __name__ == '__main__':
    move_files()
