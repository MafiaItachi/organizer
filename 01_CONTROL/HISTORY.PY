import os
from datetime import datetime

def get_video_files(folder_path, extensions):
    """Get video files from the folder with specified extensions."""
    files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if any(filename.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, filename)
                modified_time = os.path.getmtime(file_path)
                files.append((root, filename, modified_time))
    return files

def write_history_file(history_path, folder_data):
    """Write the history to a text file."""
    with open(history_path, 'w', encoding='utf-8') as f:
        f.write("✨============== FILE HISTORY ================✨\n\n")
        for folder_name, files in folder_data.items():
            f.write(f" 📁 Folder: {folder_name}\n\n")
            for file_name, modified_time in files:
                modified_str = datetime.fromtimestamp(modified_time).strftime("%d-%m-%Y")
                f.write(f"             ↪️📄 File: {file_name}➡️➡️➡️📅 Date: {modified_str}\n")
            f.write("\n==============================\n\n")
        f.write("✨==============================✨\n")

def sort_folders_by_recent_file(folder_data):
    """Sort folders based on the most recent file modified time."""
    sorted_folders = sorted(
        folder_data.items(),
        key=lambda x: max(file[1] for file in x[1]),
        reverse=True
    )
    return dict(sorted_folders)

def update_history(folder_path, history_path):
    """Update history.txt with the latest file details."""
    # Load existing history
    folder_data = {}
    if os.path.exists(history_path):
        with open(history_path, 'r', encoding='utf-8') as f:
            lines = iter(f.readlines())  # Convert lines to an iterator
        current_folder = None
        for line in lines:
            if line.startswith(" 📁 Folder:"):
                current_folder = line.split(":", 1)[1].strip()
                folder_data[current_folder] = []
            elif line.startswith("             ↪️📄 File:") and current_folder:
                file_name = line.split(":", 1)[1].split("➡️➡️➡️")[0].strip()
                modified_str = line.split("📅 Date:")[1].strip()
                modified_time = datetime.strptime(modified_str, "%d-%m-%Y").timestamp()
                folder_data[current_folder].append((file_name, modified_time))

    # Update with current folder and file data
    video_extensions = ['.mp4', '.mkv', '.avi']
    new_data = get_video_files(folder_path, video_extensions)

    for folder, file_name, modified_time in new_data:
        folder_name = os.path.basename(folder)
        if folder_name not in folder_data:
            folder_data[folder_name] = []
        if file_name not in [f[0] for f in folder_data[folder_name]]:
            folder_data[folder_name].append((file_name, modified_time))

    # Sort folders by the most recent file date
    folder_data = sort_folders_by_recent_file(folder_data)

    # Write to history.txt
    write_history_file(history_path, folder_data)

        # Print update message to terminal
    print("\n✨============= HISTORY =======================✨\n")
    print("⌛✅ History Updated")
    print("\n✨==============================================✨\n")


# Define the path to the folder and history.txt
folder_path = "C:\\VICTUS\\ENTERTANMENT"
history_path = os.path.join(folder_path, "history.txt")

# Update history.txt
update_history(folder_path, history_path)
