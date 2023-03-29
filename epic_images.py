import os
import os.path
import datetime
from pathlib import Path
from pprint import pprint

import requests
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

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
       
        save_epic_image(url, file_path, params)


def save_epic_image(url, file_path, params):
    response = requests.get(url, params)
    response.raise_for_status()
    print(response.url)
    with open (file_path, "wb") as file:
        file.write(response.content)


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
  
    api_nasa_key = os.environ["API_NASA_KEY"]
    get_epic_image(api_nasa_key)


if __name__ == "__main__":
    main()