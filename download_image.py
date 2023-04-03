import requests

def download_image(file_path, url_images):
    response = requests.get(url_images)
    response.raise_for_status()
  
    with open (file_path, "wb") as file:
        file.write(response.content)