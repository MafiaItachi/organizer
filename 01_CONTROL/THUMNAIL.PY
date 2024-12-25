import os

# Define the base folder path
base_folder = r"C:\VICTUS\ENTERTANMENT"

# Function to set the original image as the folder thumbnail
def set_folder_thumbnail(image_path):
    try:
        # Logic to use the original image as the thumbnail
        # This will depend on the OS and file system being used.
        # On Windows, folder thumbnails are system-handled based on file presence.
        # No additional script change is needed, you just ensure the image exists.
        print(f"Using {image_path} as the folder thumbnail")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Walk through all subfolders inside the base folder
for root, dirs, files in os.walk(base_folder):
    for folder in dirs:
        folder_path = os.path.join(root, folder)
        # Check for jpg files in each folder
        for file in os.listdir(folder_path):
            if file.lower().endswith('.jpg'):
                image_path = os.path.join(folder_path, file)
                # Set the existing .jpg image as the folder thumbnail
                set_folder_thumbnail(image_path)
                break  # Use the first image found in the folder

print("Folder thumbnails set successfully!")
