import os.path
import argparse
from pathlib import Path

import requests
from dotenv import load_dotenv

from download_image import download_image


def get_urls_images(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    links_images = response.json()["links"]["flickr"]["original"]
    return links_images


def fetch_spacex_all_launches(links_images, folder="images"):
    Path(folder).mkdir(parents=True, exist_ok=True)
    for number, link in enumerate(links_images):
        file_name = f"image{number}.jpeg"
        file_path = os.path.join(folder, file_name)
        download_image(file_path, link)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Загружает фотографии SpaceX"
    )
    parser.add_argument(
        '--launch_id',
        help='Id запуска',
        default="5eb87d42ffd86e000604b384"
    )
    args = parser.parse_args()
    launch_id = args.launch_id

    Path("images").mkdir(parents=True, exist_ok=True)

    links_images = get_urls_images(launch_id)
    fetch_spacex_all_launches(links_images)


if __name__ == "__main__":
    main()
