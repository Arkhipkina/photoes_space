from telegram.ext import Updater
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    updater = Updater(token = tg_token)
    print(updater.bot.get_me())
   # updater.bot.send_message(chat_id="@bot_programm", text="Здесь будут фотографии NASA")
    with open("space.jpg", "rb") as file:
        photo=file
        updater.bot.send_photo(chat_id="@bot_programm", photo=photo)

    


if __name__ == "__main__":
    main()