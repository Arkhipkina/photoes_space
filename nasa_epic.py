import os
import os.path
import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

from download_image import download_image


def get_epic_image(api_key, folder="images"):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params)
    response.raise_for_status()

    for number, epic_images in enumerate(response.json()):
        date, time = epic_images["date"].split()
        formatted_date = datetime.date.fromisoformat(date).strftime("%Y/%m/%d")
        name_image = epic_images["image"]
        
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{name_image}.png"
        
        file_name = f"EPIC{number}.png"
        file_path = os.path.join(folder, file_name)
       
        download_image(url, file_path, params)


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
  
    api_nasa_key = os.environ["API_NASA_KEY"]
    get_epic_image(api_nasa_key)


if __name__ == "__main__":
    main()
