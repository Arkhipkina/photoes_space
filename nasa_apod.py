import os
import os.path
from urllib.parse import urlsplit, unquote
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_nasa_image(api_nasa_key, folder="images"):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_nasa_key,
        "count": 30
    }
    response = requests.get(url, params)
    response.raise_for_status()
    
    for number, link in enumerate(response.json()):
        if not link["url"]:
            continue
        url_images = link["url"]
        expansion_link = get_expansion_link(url_images)
        if not expansion_link:
            continue
        file_name = f"dayimage{number}{expansion_link}"
        file_path = os.path.join(folder, file_name)
        download_image(file_path, url_images)


def download_image(file_path, url_images):
    response = requests.get(url_images)
    response.raise_for_status()
  
    with open (file_path, "wb") as file:
        file.write(response.content)


def get_expansion_link(link):
    path_image = urlsplit(unquote(link)).path
    path, full_file_name = os.path.split(path_image)
    file_name, expansion = os.path.splitext(full_file_name)
    return expansion


def main():
    load_dotenv()
    api_nasa_key = os.environ["API_NASA_KEY"]
    Path("images").mkdir(parents=True, exist_ok=True)
    get_nasa_image(api_nasa_key)
   


if __name__ == "__main__":
    main()