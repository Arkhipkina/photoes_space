import requests
import os.path
from pathlib import Path

def get_image(filename, url):
    response = requests.get(url)
    response.raise_for_status()
    print(response)
    with open (filename, "wb") as file:
        file.write(response.content)


def get_url_image():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    response.raise_for_status()
    list_links_images=[]
    for link in response.json():
        list_links_images += link["links"]["flickr"]["original"]
    return list_links_images


def fetch_spacex_all_launches(list_links_images, folder="many_images"):
    Path(folder).mkdir(parents=True, exist_ok=True)
    for number, link in enumerate(list_links_images):
        response = requests.get(link)
        response.raise_for_status()
        file_name = f"image{number}.jpeg"
        file_path = os.path.join(folder, file_name)
        with open (file_path, "wb") as file:
            file.write(response.content)
    

def main():
    Path("images").mkdir(parents=True, exist_ok=True)
  
    filename = "images/hubble.jpeg"
    url = "https://api.spacexdata.com/v5/launches/latest"
  
    get_image(filename, url)
    list_links_images = get_url_image()
    fetch_spacex_all_launches(list_links_images)

if __name__ == "__main__":
    main()