import random
import os
from time import sleep

from telegram.ext import Updater
from dotenv import load_dotenv




def get_random_path_image(folder="images"):
    images = os.listdir(folder)
    random.shuffle(images)
    path_images = [os.path.join(folder, image) for image in images]
    return path_images


def get_piblish_photoes(updater, delay_time):
    while True:
        path_images = get_random_path_image()
        for path_image in path_images:
            with open(path_image, "rb") as file:
                photo=file
                updater.bot.send_photo(chat_id="@bot_programm", photo=photo)
            sleep(delay_time)


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    updater = Updater(token = tg_token)
    delay_time = os.environ["DELAY_TIME"]
    get_piblish_photoes(updater, int(delay_time))
    


if __name__ == "__main__":
    main()