# Загрузка фоографий космоса в Telegram
В данном проекте Вы сможете загрузить фотографии NASA в Telegram-канал.

## Как установить 
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```

## Переменная окружения

Переменные окружения - это текстовые переменные с динамическими именем, которые могут влиять на поведение запущенных процессов на компьютере/в коде.
Чтобы получить и оформить переменные окружения, которые используются в этом коде Вам необходимо:
1. Получите API-ключ на сайте [api.nasa.gov](https://api.nasa.gov/) и запишите его в переменную `API_NASA_KEY`.
2. Получить Telegram-токен у [Отца ботов](https://t.me/BotFather) и запишите его в переменную `TG_TOKEN`.
3. Понять какое время задержки Вы хотите поставить для публикации фотографий (в секундах) и запишите его в переменную `DELAY_TIME`.
4. Создайте файл `.env`
5. Заполните `.env` файл согласно примеру:

```python
API_NASA_KEY=*Ваш токен*
TG_TOKEN=*Ваш токен*
DELAY_TIME=*Ваше время*
```

## Как запустить

Если Вы хотите загрузить фотографии SpaceX:

Если Вы хотите загрзить фотографии последнего запуска:
```python
python fetch_spacex_images.py
```

Если Вы хотите загрузить фотографии любого другого запуска:
```python
python fetch_spacex_images.py --launch_id *id запуска*
```

Если Вы хотите загрузить фотографии APOD:

```python
python nasa_apod.py
```

Если Вы хотите загрузить фотографии EPIC:

```python
python nasa_epic.py
```

Если Вы хотите опубликовать фотографии:

```python
python telegram-channel.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
