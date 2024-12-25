import os
import time
import subprocess

def update_mkv_metadata(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mkv'):
                file_path = os.path.join(root, file)
                new_title = os.path.splitext(file)[0]  # Extract the filename without extension

                # Get the original access and modification times
                original_atime = os.path.getatime(file_path)  # Last access time
                original_mtime = os.path.getmtime(file_path)  # Last modified time

                try:
                    # Run mkvpropedit to update metadata
                    result = subprocess.run(
                        ["mkvpropedit", file_path, "--edit", "info", "--set", f"title={new_title}"],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                    )

                    # Check the output of mkvpropedit for confirmation of changes
                    if "The changes are written to the file." not in result.stdout:
                        print(f"No changes needed for: {file}")

                    # Restore the original timestamps
                    os.utime(file_path, (original_atime, original_mtime))

                except subprocess.CalledProcessError as e:
                    print(f"Failed to update metadata for: {file}. Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred for: {file}. Error: {e}")

# Specify the directory containing the .mkv files
directory_path = r"C:\VICTUS\ENTERTANMENT"  # Replace with your directory
update_mkv_metadata(directory_path)
