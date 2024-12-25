import os
import requests
from PIL import Image
from io import BytesIO
import urllib.parse
import json
import re
from tqdm import tqdm  # Import tqdm for progress bar

def prettify_response(data):
    """Prettifies the API response into a readable format with emojis."""
    try:
        title = data.get("Title", "Unknown")
        year = data.get("Year", "Unknown")
        rated = data.get("Rated", "Unknown")
        released = data.get("Released", "Unknown")
        runtime = data.get("Runtime", "Unknown")
        genre = data.get("Genre", "Unknown")
        actors = data.get("Actors", "Unknown").split(", ")
        plot = data.get("Plot", "Unknown")
        language = data.get("Language", "Unknown")
        country = data.get("Country", "Unknown")
        awards = data.get("Awards", "None")
        poster_url = data.get("Poster", "No Poster Available")
        imdb_rating = data.get("imdbRating", "N/A")
        imdb_votes = data.get("imdbVotes", "N/A")
        imdb_id = data.get("imdbID", "N/A")
        total_seasons = data.get("totalSeasons", "N/A")

        response = f"""
🎥 **Title:** {title}  
📅 **Year:** {year}  
⭐ **Rated:** {rated}  
📆 **Released:** {released}  
⏳ **Runtime:** {runtime}  
🎭 **Genre:** {genre}  

👨‍🎤 **Actors:**  
{chr(10).join(f"- {actor}" for actor in actors)}  

📖 **Plot:**  
> {plot}  

🗣️ **Languages:** {language}  
🌍 **Country:** {country}  

🏆 **Awards:**  
{awards}  

🔗 **Poster URL:**  
[{poster_url}]({poster_url})  

📊 **Ratings:**  
- **IMDB Rating:** {imdb_rating}  
- **IMDB Votes:** {imdb_votes}  

🎬 **IMDB Details:**  
- **ID:** {imdb_id}  
- **Total Seasons:** {total_seasons}  
        """
        return response.strip()
    except Exception as e:
        return f"Error formatting response: {e}"

def fetch_poster(title, year, save_path, response_path, success_titles, not_found_titles):
    """Fetches the poster of a movie/TV show by title and year, and saves it to the specified path."""
    api_key = "38d2ac41"  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={urllib.parse.quote(title)}&y={year}&apikey={api_key}" if year else f"http://www.omdbapi.com/?t={urllib.parse.quote(title)}&apikey={api_key}"

    try:
        if os.path.exists(save_path) and os.path.exists(response_path):
            success_titles.append(title)
            return  # Skip processing if both files already exist

        response = requests.get(url)
        data = response.json()

        # Save the prettified response to a text file
        prettified = prettify_response(data)
        response_path = response_path.replace("{title}", title)
        save_path = save_path.replace("{title}", title)
        with open(response_path, "w", encoding="utf-8") as f:
            f.write(prettified)

        if data["Response"] == "True" and "Poster" in data and data["Poster"] != "N/A":
            poster_url = data["Poster"]
            poster_response = requests.get(poster_url)
            poster_image = Image.open(BytesIO(poster_response.content))

            # Save the poster
            poster_image.save(save_path)
            success_titles.append(title)
        else:
            not_found_titles.append(title)

    except Exception as e:
        print(f"Error fetching poster for '{title}': {e}")
        not_found_titles.append(title)

def extract_title_and_year(folder_name):
    """Extracts the title and year from a folder name if a year is present."""
    match = re.search(r"(.*?)(\d{4})", folder_name)
    if match:
        title = match.group(1).strip()
        year = match.group(2)
    else:
        title = folder_name
        year = None
    return title, year

def main():
    base_directory = r"C:\VICTUS\ENTERTANMENT"  # Replace with the path to your directory

    success_titles = []
    not_found_titles = []

    # List folders for processing and use tqdm for progress bar
    folders = [folder_name for folder_name in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, folder_name))]
    
    # Initialize tqdm with emojis
    progress_bar = tqdm(
        folders,
        desc="🚀 Downloading Poster",
        unit="folder",
        bar_format="{l_bar}{bar} 📁 {n_fmt}/{total_fmt} {elapsed}",
        ascii=False,
        ncols=100
    )
    
    for folder_name in progress_bar:
        folder_path = os.path.join(base_directory, folder_name)

        response_path = os.path.join(folder_path, "Detail - {title}.txt")
        poster_path = os.path.join(folder_path, "0_Poster - {title}.jpg")

        # Fetch and save poster and details
        fetch_poster(*extract_title_and_year(folder_name), poster_path, response_path, success_titles, not_found_titles)

    # Print results
    if not_found_titles:
        print(f"\n⚠️============== 🚨 NOT FOUND 🚨 ==============⚠️")
        print("📁 Poster could not be found.")
        for title in not_found_titles:
            print(f"🎥 Title: {title}")
        print(f"⚠️=============================================⚠️\n")

    if success_titles:
        print(f"\n✨=============== 🎉 SUCCESS 🎉 ==============✨")
        print("📁 Poster and Details are saved successfully!")
        for title in success_titles:
            print(f"ℹ️ Saved for : {title}")
        print(f"✨=============================================✨\n")

if __name__ == "__main__":
    main()
