import random
import os
from time import sleep

import requests
import telegram
from telegram.ext import Updater
from dotenv import load_dotenv




def get_random_path_image(folder="images"):
    images = os.listdir(folder)
    random.shuffle(images)
    path_images = [os.path.join(folder, image) for image in images]
    return path_images


def get_publish_photoes(updater, delay_time, tg_chat_id):
    while True:
        try:
            path_images = get_random_path_image()
            for path_image in path_images:
                with open(path_image, "rb") as file:
                    photo=file
                    updater.bot.send_photo(tg_chat_id, photo=photo)
                sleep(delay_time)
        except telegram.error.NetworkError("Нет интернета!"):
            sleep(20)


def main():
    load_dotenv()
    tg_chat_id = os.environ["tG_CHAT_ID"]
    tg_token = os.environ["TG_TOKEN"]
    updater = Updater(token = tg_token)
    delay_time = os.getenv("DELAY_TIME", default=14400)
    get_publish_photoes(updater, int(delay_time), tg_chat_id)
    


if __name__ == "__main__":
    main()