# Media Organizer and OMDb Integration Script

## Overview
This Python script streamlines the process of organizing and enriching your media library. It not only organizes movie and TV show files into structured folders but also integrates with the OMDb API to fetch and save detailed information and posters for each title.

## Features

### **Media File Organization**
- Automatically organizes files into folders based on their names and metadata (e.g., "Movie Title (Year)").
- Handles common patterns like "SxxExx" for TV shows or "1080p" for resolution.
- Ensures folder names are neatly formatted:
  - Dots (`.`) in names are replaced with spaces.
  - Unwanted tags like "1080p" are removed.
  - Prioritizes folders with a year in their name when duplicates exist.

### **OMDb API Integration**
- **Fetch Movie/TV Details**: Queries the OMDb API for metadata like genre, release date, director, and more.
- **Poster Download**: Saves the official poster image as `0_Poster - {title}.jpg`.
- **Details File**: Generates a neatly formatted text file (`Detail - {title}.txt`) with all relevant metadata.
- **Efficiency**: Skips processing if the poster and details file already exist in the folder.

### **User Feedback**
- Clear terminal messages for processed items.
- Informs you about missing data (e.g., if a poster is unavailable).

### **Customization Options**
- Easily configurable base directory.
- Supports extensions like `.mkv`, `.mp4`, `.avi`.
- OMDb API key integration for fetching data.

## Requirements
- Python 3.x
- Libraries:
  - `os`
  - `shutil`
  - `re`
  - `requests` (for API calls)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/media-organizer.git
   ```
2. Install required libraries:
   ```bash
   pip install requests
   ```
3. Set up your OMDb API key:
   - Replace `YOUR_API_KEY` in the script with your actual OMDb API key.

## Usage
1. Update the `source_directory` in the script to point to your media folder.
2. Run the script:
   ```bash
   python media_organizer.py
   ```
3. Organized files and additional metadata will appear in the respective folders.

## Example Output
```
✨==============================✨
 📂 Folder Created : Inception 2010
 ↪️📁 Edited Movie Name: INCEPTION 2010.mkv
 ↪️📄 Detail File: Detail - INCEPTION.txt
 ↪️🖼️ Poster File: 0_Poster - INCEPTION.jpg
✨==============================✨
```

## Visual Overview
Below is an example of how your organized folders might look:

![image](https://github.com/user-attachments/assets/e8867d67-4226-494c-8149-c73b3148e765)
![image](https://github.com/user-attachments/assets/64910109-fb9e-4452-97dc-8f232978780a)
![image](https://github.com/user-attachments/assets/cd860dc0-7b3d-4466-8f95-fb0268c1cef7)
![image](https://github.com/user-attachments/assets/575e1d0e-1419-401e-b98a-ea1a485d789f)




## Contribution
Feel free to fork and submit pull requests for improvements or new features!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
**Happy organizing!** 😊

