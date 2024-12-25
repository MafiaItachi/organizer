import os
from pymediainfo import MediaInfo

def update_video_title(file_path):
    # Get the file name without the extension
    file_name = os.path.basename(file_path)
    name_without_extension = os.path.splitext(file_name)[0]

    # Load the media information
    media_info = MediaInfo.parse(file_path)

    # Check if the title metadata can be updated
    for track in media_info.tracks:
        if track.track_type == "General":
            # Update title metadata
            track.title = name_without_extension
            print(f"✅ Title updated: '{file_name}'➡️🏷️ '{name_without_extension}'")
            return True
    print(f"⚠️ Unable to update the title for: '{file_name}'")
    return False


def process_folder(folder_path):
    print("✨\n============== TITTLE UPDATE =================✨")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Only process video files based on their extensions
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv')):
                file_path = os.path.join(root, file)
                update_video_title(file_path)
    print("\n")
    print("🎉 All files processed! Titles renamed")
    
    print("\n✨=============================================✨")


# Example usage
folder_path = r"C:\\VICTUS\\ENTERTAINMENT"
process_folder(folder_path)
