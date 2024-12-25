import os
import subprocess
c

def update_metadata_to_filename(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mkv', '.mp4', '.avi', '.mov')):
                file_path = os.path.join(root, file)
                new_title = os.path.splitext(file)[0]  # Get the filename without extension
                
                # Get the original timestamps
                original_atime = os.path.getatime(file_path)  # Last access time
                original_mtime = os.path.getmtime(file_path)  # Last modified time

                # Wrap paths with quotes to handle spaces
                file_path_quoted = f'"{file_path}"'
                temp_file = os.path.join(root, f"temp_{file}")
                temp_file_quoted = f'"{temp_file}"'

                try:
                    # Run FFmpeg command
                    subprocess.run(
                        f'ffmpeg -i {file_path_quoted} -metadata title="{new_title}" -c copy {temp_file_quoted}',
                        check=True, shell=True
                    )
                    
                    # Replace original file with updated file
                    os.replace(temp_file, file_path)

                    # Restore original timestamps
                    os.utime(file_path, (original_atime, original_mtime))
                    
                    print(f"Updated metadata for: {file}")
                except Exception as e:
                    print(f"Failed to update metadata for: {file}. Error: {e}")
                finally:
                    # Clean up temp file if it exists
                    if os.path.exists(temp_file):
                        os.remove(temp_file)

# Specify the directory containing the media files
directory_path = r"C:\VICTUS\ENTERTANMENT"
update_metadata_to_filename(directory_path)
